from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Post


class PostListView(ListView):
    model = Post
