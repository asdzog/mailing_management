from django.views.generic import ListView

from blog.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
