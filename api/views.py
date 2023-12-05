from rest_framework import viewsets

from .serializers import BookmarkViewSetSerializer
from bookmark.models import Bookmark

class BookmarkViewSet(viewsets.ModelViewSet):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkViewSetSerializer