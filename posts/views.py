from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

class PostListView(ListView):
    model = Post
    template_name= "posts_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class TestView(ListView):
    model = Post
    template_name = 'test.html'