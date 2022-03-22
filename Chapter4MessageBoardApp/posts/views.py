from django.views.generic import ListView

from posts.models import Posts


class HomePageView(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name = 'all_post_name'
