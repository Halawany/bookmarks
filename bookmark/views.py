from django.views.generic import ListView

from .models import Bookmark

class HomeView(ListView):
    
    model = Bookmark
    template_name = "bookmark/home.html"
    context_object_name = 'bookmarks'