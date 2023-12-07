from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import BookmarkSerializer, BookmarkUpdateViewSerializer

from bookmark.models import Bookmark
from .permissions import IsAuthorOrReadOnly

class BookmarkListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(author=user)

class BookmarkUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkUpdateViewSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(author=user)

class BookmarkDeleteAPIView(generics.RetrieveDestroyAPIView):
    
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(author=user)

