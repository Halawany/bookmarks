from rest_framework import serializers

from bookmark.models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"

class BookmarkUpdateViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('title', 'url')