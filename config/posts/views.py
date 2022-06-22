from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers, UserSerializer
from rest_framework import generics, permissions, viewsets
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model # new
from .forms import PostForm
from django.views.generic import FormView #new

from django.views.generic.edit import CreateView, UpdateView #new


#class BlogCreateView(CreateView):
    #model = Post
    #template_name = 'post_new.html'
    #fields = ['title', 'author', 'body']
    

    
"""def create_custom_project(request):
    print('Cliecked Create Custom Project')
    if request.method == "POST":
        form = CustomProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("thank_you")"""

"""class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializers"""
    
class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
    
class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model
    serializer_class = UserSerializer
    
    
#class PostFormView(FormView):
    #template = 'posts/new_post.html'
    #form_class = PostForm
    
    

    
    
