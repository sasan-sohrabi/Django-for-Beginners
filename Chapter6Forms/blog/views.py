from django.views.generic import ListView, DetailView

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'page_detail.html'