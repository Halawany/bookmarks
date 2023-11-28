from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, BookmarkUpdateView, DeleteBookmark, NewBookmark, SearchView

urlpatterns = [
    path('', HomeView.as_view(), name='bookmarks'),
    path('edit-bookmark/<int:pk>', BookmarkUpdateView.as_view(), name='edit_bookmark'),
    path('delete/<int:pk>', DeleteBookmark.as_view(), name='delete_bookmark'),
    path('new-bookmark', NewBookmark.as_view(), name='new_bookmark'),
    path('search/', SearchView.as_view(), name='search_bookmark'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
