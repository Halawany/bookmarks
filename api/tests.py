from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from bookmark.models import Bookmark

class BookmarkAPITest(APITestCase):
    def setUp(self):
        self.joe = get_user_model().objects.create_user(username='joe', password='password')
        self.john = get_user_model().objects.create_user(username='john', password='password')
        user_1 = get_user_model().objects.get(id=1)
        user_2 = get_user_model().objects.get(id=2)
        api_data = Bookmark.objects.create(
            title="Test title",
            url="https://www.test.com",
            author=user_1
        )
        api_data_2 = Bookmark.objects.create(
            title="Test title 2",
            url="https://www.testuser2.com",
            author=user_2
        )

    
    def test_get_api_data(self):
        """ Retrieve API Data without authentication must return 403 Forbidden"""
        response = self.client.get(reverse('bookmark_api_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_get_api_data_authenticated(self):
        """Retrieve API Data with authentication must return 200 OK"""
        self.client.force_login(self.joe)
        response = self.client.get(reverse('bookmark_api_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_api_data_unauthenticated(self):
        """Update api data like '/api/bookmark/1' without authentication must return 403 Forbidden"""
        response = self.client.get(reverse('bookmark_api_update', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_api_data_authenticated(self):
        self.client.force_login(self.joe)
        data = {'title': 'New title after update',
        'url': 'https://www.newtest.com'}
        response = self.client.put(
            reverse('bookmark_api_update', kwargs={'pk':1}), 
        data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Bookmark.objects.get(id=1).title, 'New title after update')
        self.assertEqual(Bookmark.objects.get(id=1).url, 'https://www.newtest.com')

    def test_delete_api_data_unauthenticated(self):
        """Delete api data like '/api/delete/1' without authentication must return 403 Forbidden"""
        response = self.client.get(reverse('bookmark_api_delete', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_delete_api_data_authenticated(self):
        """Delete api data like '/api/delete/1' with authentication must return 204 No Content"""
        self.client.force_login(self.joe)
        response = self.client.delete(reverse('bookmark_api_delete', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_get_api_data_authenticated_by_another_user(self):
        """Retrieve user_1 data authenticated by another user must return user_2 data"""
        self.client.force_login(self.john)
        response = self.client.get(reverse('bookmark_api_list'), format='json')
        self.assertEqual(response.data[0]["title"], 'Test title 2')

    def test_update_api_data_authenticated_by_another_user(self):
        """Update user 1 data authenticated by anoter user 'user_2' must return 404 Not found"""
        self.client.force_login(self.john)
        data = {'title': 'New title after update',
        'url': 'https://www.newtest.com'}
        response = self.client.put(reverse('bookmark_api_update', kwargs={'pk':1}),
        data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_api_data_authenticated_by_another_user(self):
        """Delete user_1 data authenticated by another user must return 404 Not Found"""
        self.client.force_login(self.john)
        response = self.client.delete(reverse('bookmark_api_delete', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)