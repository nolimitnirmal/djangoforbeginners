from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostList(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"


def about(request):
    return render(request, "about.html")
