from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, BookmarkUpdateView, DeleteBookmark

urlpatterns = [
    path('', HomeView.as_view(), name='bookmarks'),
    path('edit-bookmark/<int:pk>', BookmarkUpdateView.as_view(), name='edit_bookmark'),
    path('delete/<int:pk>', DeleteBookmark.as_view(), name='delete_bookmark'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
