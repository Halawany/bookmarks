from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..models import Bookmark

class TestBookmarksView(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(username='test_user', password='@Test123456')
        self.user_2 = get_user_model().objects.create_user(username="test_user_2", password="@Test123456")

        user = get_user_model().objects.get(id=1)
        user_2 = get_user_model().objects.get(id=2)

        bookmark = Bookmark.objects.create(
            title='Test Bookmark', 
            url="https://www.google.com",
            author=user
            )
        bookmark_2 = Bookmark.objects.create(
            title='New Test Bookmark', 
            url="https://www.facebook.com",
            author=user_2
            )
    
    def test_authentication_view(self):

        """Testing user credentials in login view"""

        self.client.force_login(self.user)
        response = self.client.get('/accounts/login')
        self.assertTemplateUsed('home.html')

    def test_hompage_authentication_required(self):

        """When user requests homepage, the server should redirect him to login page"""
        
        response = self.client.get(reverse('bookmarks'))
        self.assertEqual(response.status_code, 302)
    
    def test_edit_bookmark_authentication_required(self):

        """When user requests edit bookmark, the server should redirect him to login page"""
        
        response = self.client.get(reverse('edit_bookmark', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_bookmark_authentication_required(self):

        """When user delete a bookmark without authentication, the server should redirect him to login page"""
        
        response = self.client.get(reverse('delete_bookmark', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 302)

    def test_new_bookmark_authentication_required(self):

        """When user requests a new bookmark page, the server should redirect him to login page"""
        
        response = self.client.get(reverse('new_bookmark'))
        self.assertEqual(response.status_code, 302)

    def test_user_homepage_authentication(self):

        """Test user Authentication to homepage"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('bookmarks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bookmark")
        self.assertTemplateUsed(response, "bookmark/home.html")

    def test_user_can_edit_bookmark(self):

        """Test user can edit his own bookmarks"""
        self.client.force_login(self.user)
        response = self.client.get('/edit-bookmark/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit Bookmark")
        self.assertTemplateUsed(response, "bookmark/edit.html")
    
    def test_user_can_delete_bookmark(self):

        """Test user can delete his own bookmarks"""
        self.client.force_login(self.user)
        response = self.client.get('/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete Bookmark, Are you sure?")
        self.assertTemplateUsed(response, "bookmark/delete.html")
    
    def test_user_cant_get_other_users_bookmarks(self):

        """User can't see other users's bookmarks"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('bookmarks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookmark/home.html")
        self.assertNotContains(response, "New Test Bookmark")
    
    def test_user_cant_edit_other_users_bookmarks(self):

        """User can't edit other users's bookmarks"""
        self.client.force_login(self.user)
        response = self.client.get('edit-bookmark/2')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, "bookmark/edit.html")
    
    def test_user_cant_delete_other_users_bookmarks(self):

        """User can't delete other users's bookmarks"""
        self.client.force_login(self.user)
        response = self.client.get('delete/2')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, "bookmark/delete.html")
