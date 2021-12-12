from django.urls import path
from .views import (
    PostListView, 
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)

app_name='blog'
urlpatterns = [
    path('posts/',PostListView.as_view(), name='post_list'),
    path('create-posts/',PostCreateView.as_view(), name='create_posts'),
    path('post-details/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]