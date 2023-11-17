from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Bookmark

class HomeView(LoginRequiredMixin, ListView):
    
    model = Bookmark
    template_name = "bookmark/home.html"
    context_object_name = 'bookmarks'

    def get_queryset(self):
        query_Set = Bookmark.objects.filter(author=self.request.user)
        return query_Set

class NewBookmark(LoginRequiredMixin, CreateView):
    
    model = Bookmark
    template_name = "bookmark/new.html"
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmarks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class BookmarkUpdateView(LoginRequiredMixin, UpdateView):

    model = Bookmark
    template_name = "bookmark/edit.html"
    fields = ["title", "url"]
    success_url = reverse_lazy('bookmarks')

    def get_queryset(self):
        user_bookmarks = Bookmark.objects.filter(author=self.request.user)
        return user_bookmarks
    

class DeleteBookmark(LoginRequiredMixin, DeleteView):

    model = Bookmark
    template_name = "bookmark/delete.html"
    success_url = reverse_lazy('bookmarks')