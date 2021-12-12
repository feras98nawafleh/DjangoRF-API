from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'timestamp', 'updated', 'author', 'published']

admin.site.register(Post)
