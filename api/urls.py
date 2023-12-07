from django.urls import path, include

from .views import BookmarkListCreateAPIView, BookmarkUpdateAPIView, BookmarkDeleteAPIView

urlpatterns = [
    path('', BookmarkListCreateAPIView.as_view(), name="bookmark_api_list"),
    path('update/<int:pk>', BookmarkUpdateAPIView.as_view(), name="bookmark_api_update"),
    path('delete/<int:pk>', BookmarkDeleteAPIView.as_view(), name="bookmark_api_delete")
]
