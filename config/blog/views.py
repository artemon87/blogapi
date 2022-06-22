from django.shortcuts import render
from .forms import BlogPostForm
from django.views.generic import FormView #new

from django.views.generic.edit import CreateView, UpdateView #new

class BlogCreateView(FormView):
    template_name = 'blogpost_new.html'
    form_class = BlogPostForm
    success_url = 'blogpost'
    

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        print(form)
        return super().form_valid(form)
