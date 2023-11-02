from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Bookmark

class HomeView(ListView):
    
    model = Bookmark
    template_name = "bookmark/home.html"
    context_object_name = 'bookmarks'

class BookmarkUpdateView(UpdateView):

    model = Bookmark
    template_name = "bookmark/edit.html"
    fields = ["title", "url"]
    success_url = reverse_lazy('bookmarks')

class DeleteBookmark(DeleteView):

    model = Bookmark
    template_name = "bookmark/delete.html"
    success_url = reverse_lazy('bookmarks')