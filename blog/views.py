from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Post
from django.views.generic import ListView

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'