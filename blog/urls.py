from django.urls import path

from blog.views import PostListView
from blog.apps import PostConfig

app_name = PostConfig.name

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
]
