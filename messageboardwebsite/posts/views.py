from django.shortcuts import render  # import render shortcut function
from django.views.generic import ListView  # import listview

from .models import Post


class PostList(ListView):  # new post class to extend list view
    model = Post  # define the desired model
    template_name = "post_list.html"  # deifne template name
    context_object_name = "posts"  #


def about(request):
    return render(request, "about.html")
