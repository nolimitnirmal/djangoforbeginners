from django.urls import path
from .views import PostList, about

urlpatterns = [
    path(
        "", PostList.as_view(), name="home"
    ),  # as_view() method to return a callable view.
    path("about/", about, name="about"),
]
