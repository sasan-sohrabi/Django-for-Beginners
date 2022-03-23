from django.urls import path

from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('page_detail/<int:pk>/', BlogDetailView.as_view(), name='page_detail'),
    path('', BlogListView.as_view(), name='home')
]
