from django.contrib import admin
from .models import BlogPost, Field
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'body', 'created_at')
    list_filter = ('title',)
    ordering = ('-title',)
    
    
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'name')
    list_filter = ('name',)
    ordering = ('-name',)
    
admin.site.register(Field, FieldAdmin)
admin.site.register(BlogPost, BlogAdmin)