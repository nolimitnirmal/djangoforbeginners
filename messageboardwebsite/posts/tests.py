from django.test import TestCase
from django.urls import reverse                          
from .models import Post 

# first import testcase and post model

# Create your tests here.


class PostTests(TestCase):  # new class extends testcase and uses built in method setuptestdata to develop initial data 
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")     

    def test_url_exists_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response,"This is a test!")

