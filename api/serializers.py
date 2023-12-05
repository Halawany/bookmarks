from rest_framework import serializers

from bookmark.models import Bookmark

class BookmarkViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"