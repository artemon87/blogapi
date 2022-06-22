from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    def clean(self):
        if 'author' in self.cleaned_data:
            print('Author is {}'.format(self.cleaned_data['author']))
        print("self.cleaned_data: {}".format(self.cleaned_data))
        return self.cleaned_data


    class Meta:
        model = BlogPost
        fields = (
            'title', 'body',
        )
        required = (
             'title', 'body',
        )