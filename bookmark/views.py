from django.views.generic import TemplateView

from .models import Bookmark

class HomeView(TemplateView):
    
    template_name = "bookmark/home.html"
