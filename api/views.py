from rest_framework import generics

from .serializers import BookmarkViewSetSerializer
from bookmark.models import Bookmark

class BookmarkListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkViewSetSerializer