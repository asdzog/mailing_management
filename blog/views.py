from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'slug', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:blog_view')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.save()

        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'views_count', 'content', 'preview', 'date_published', 'is_active')
    success_url = reverse_lazy('blog:blog_view')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.save()

        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_view')
