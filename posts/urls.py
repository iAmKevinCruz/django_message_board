from django.urls import path
from .views import (
    HomePageView, 
    PostListView, 
    PostDetailView,
    TestView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='all_posts'),
    path('test/', TestView.as_view(), name='test'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]