from django.shortcuts import render
from .models import *
from frontend import *
from django.views.generic import *

def indexx(request):
    posts = Post.objects.all()
    
    content = {
        "posts": posts
    }
    return render(request, 'index.html', content)

class AboutView(TemplateView):
    template_name = 'about.html'
class ContactView(TemplateView):
    template_name = 'contact.html'
class AuthorView(TemplateView):
    template_name = 'author.html'
class IndexfullView(TemplateView):
    template_name = 'index-full.html'
class IndexfullleftView(TemplateView):
    template_name = 'index-full-left.html'
class IndexfullrightView(TemplateView):
    template_name = 'index-full-right.html'
class IndexlistView(TemplateView):
    template_name = 'index-list.html'