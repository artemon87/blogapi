from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def clean(self):
        if 'author' in self.cleaned_data:
            print('Author is {}'.format(self.cleaned_data['author']))
        return self.cleaned_data


    class Meta:
        model = Post
        fields = (
            'title', 'body',
        )
        required = (
             'title', 'body',
        )
