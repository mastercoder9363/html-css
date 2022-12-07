from django.contrib import admin

from .models import *



@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date')