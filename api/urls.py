from django.urls import path, include

from .views import BookmarkListCreateAPIView, BookmarkUpdateAPIView, BookmarkDeleteAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('', BookmarkListCreateAPIView.as_view(), name="bookmark_api_list"),
    path('update/<int:pk>', BookmarkUpdateAPIView.as_view(), name="bookmark_api_update"),
    path('delete/<int:pk>', BookmarkDeleteAPIView.as_view(), name="bookmark_api_delete"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


