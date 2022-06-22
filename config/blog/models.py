from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # new

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse('blogpost_detail', args=[str(self.id)])
    
class Field(models.Model):
    blog = models.ForeignKey(BlogPost, 
                            related_name="blogpost_field", 
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True)
    name = models.CharField(max_length=140, null=True)
    
    def __str__(self):
        return self.name + " : " + str(self.blog)
