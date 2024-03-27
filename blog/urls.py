from django.urls import path

from blog.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from blog.apps import PostConfig

app_name = PostConfig.name

urlpatterns = [
    path('blog_view', PostListView.as_view(), name='blog'),
    path('post_create', PostCreateView.as_view(), name='post_create'),
    path('post_view/<int:pk>/', PostDetailView.as_view(), name='post_view'),
    path('post_edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
