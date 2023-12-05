from rest_framework import routers

from .views import BookmarkViewSet

router = routers.SimpleRouter()
router.register('bookmarks', BookmarkViewSet, basename="bookmarks_api")
urlpatterns = router.urls
