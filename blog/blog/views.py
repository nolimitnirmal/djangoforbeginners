from django.shortcuts import render, get_object_or_404# imports djangos helper for rendering the html template
from .models import Post # imports Post model from the current app models.

# Create your views here.

def post_list(request): # defines a function based view thatrecieves the browsers http request. 
    posts = Post.objects.all() # retrieves all of the post record from the database. 
    return render(request, 'home.html', {'posts' : posts}) # suppliest those records under the same name posts 


def post_detail(request, pk): # defines a function based view thatrecieves the browsers http request. 
    post = get_object_or_404(Post, pk=pk) # retrieves the requested post from the database. 
    return render(request, "post_detail.html", {"post": post}) # supplies the record under the name post
