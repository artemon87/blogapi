from django.test import TestCase
from django.urls import reverse
from .models import BlogPost
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogpostTests(TestCase):
    def setUp(self):
        url = reverse('blogpost_new')
        self.response = self.client.get(url)
        
    def test_blogpost_page(self):
        self.assertEqual(self.response.status_code, 200)
        #self.assertTemplateUsed(self.response, 'signup.html')
        #self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')


# Sample tests here
"""class BlogpostTests(TestCase):
    def setUp(self):
        self.blogpost = BlogPost.objects.create(
            author = User.objects.first(), 
            body = "Blogpost Body",
            title = "My Blogpost title"
            )
        
    def test_regular_blog_post(self):
        #self.assertEqual(f"{self.blogpost.author.username}", "artemon87")
        self.assertEqual(f"{self.blogpost.body}", "Blogpost Body")
        
        

"""