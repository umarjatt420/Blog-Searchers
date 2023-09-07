from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'picture', 'category', 'datetime', 'heading', 'content']
