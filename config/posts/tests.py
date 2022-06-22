

from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='art',
            email='art@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'art')
        self.assertEqual(user.email, 'art@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        
    def test_create_superuser(self):    
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        
        
from django.urls import reverse # new
#from .forms import CustomUserCreationForm # new#
class SignupPageTests(TestCase): # new
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
        
    def test_signup_form(self): # new
        form = self.response.context.get('form')
        #self.assertIsInstance(form, CustomUserCreationForm)