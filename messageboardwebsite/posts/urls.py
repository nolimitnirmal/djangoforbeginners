from django.urls import path
from .views import PostList, about

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("about/", about, name="about"),
]
