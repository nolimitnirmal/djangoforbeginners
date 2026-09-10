from django.views.generic import ListView, DetailView # import pre-built classes from django views
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# ListView -display a list of object    
# DetailView - display one specific object 
from .models import Post # import the post database form models.    

# Create your views here.

class BlogListView(ListView): # creating a BlogListView and it inherits from Djangis Class View 
    model = Post # recieve the objects from the post model. 
    template_name = "home.html" # after getting the posts, display them using home.html 
    context_object_name = 'posts'

class BlogDetailView(DetailView): # create a BlogDetailView class using djangos DetailView Class View,
    model = Post # receive the objects from post model. 
    template_name = "post_detail.html" # display the posts on post_detail.html

class BlogCreateView(CreateView): 
    model = Post # 
    template_name = "post_new.html" 
    fields = ["title","author","body"]

class BlogUpdateView(UpdateView): 
    model = Post # 
    template_name = "post_edit.html" 
    fields = ["title","body"]

class BlogDeleteView(DeleteView): 
    model = Post # 
    template_name = "post_delete.html" 
    success_url = reverse_lazy("home")

