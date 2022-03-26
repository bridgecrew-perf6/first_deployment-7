from django.contrib import admin

from .forms import SetPassword, SignupForm
from . models import Post
# Register your models here.
@admin.register(Post)
class BlogPost(admin.ModelAdmin):
    list_display=['id','title','desc']


