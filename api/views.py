from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import BookmarkSerializer, BookmarkUpdateViewSerializer

from bookmark.models import Bookmark
from .permissions import IsAuthorOrReadOnly

class BookmarkListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(author=user)
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class BookmarkUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkUpdateViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(author=user)

class BookmarkDeleteAPIView(generics.RetrieveDestroyAPIView):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(author=user)

