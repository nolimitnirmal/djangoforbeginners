from django.urls import path
from .views import home_page_view, AboutPageView

urlpatterns = [path("", home_page_view), path("about/", AboutPageView.as_view())]
