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