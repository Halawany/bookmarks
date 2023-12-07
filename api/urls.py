from django.urls import path, include

from .views import BookmarkListCreateAPIView

urlpatterns = [
    path('', BookmarkListCreateAPIView.as_view(), name="bookmark_api_list"),
]
