from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookmark.urls')),
    path('api/', include('api.urls'), name='api'),
    path('accounts/', include('allauth.urls'))
]
