from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, BookmarkUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home_bookmark'),
    path('edit-bookmark/<int:pk>', BookmarkUpdateView.as_view(), name='edit_bookmark'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
