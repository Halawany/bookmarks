from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, BookmarkDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('edit-bookmark/<int:pk>', BookmarkDetailView.as_view(), name='bookmark-edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
