
from django.urls import path #import path module to view post_list
from .views import post_detail, post_list #

urlpatterns = [
    path("", post_list, name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]
