from django.views.generic import ListView, UpdateView

from .models import Bookmark

class HomeView(ListView):
    
    model = Bookmark
    template_name = "bookmark/home.html"
    context_object_name = 'bookmarks'

class BookmarkDetailView(UpdateView):

    model = Bookmark
    template_name = "bookmark/home.html"
    fields = ["title", "url"]