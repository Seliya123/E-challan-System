from django.contrib import admin

# Register your models here.

from .models import Post, challans

admin.site.register(challans)

admin.site.register(Post)