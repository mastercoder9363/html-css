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
class IndexlistleftView(TemplateView):
    template_name = 'index-list-left.html'
class IndexlistrightView(TemplateView):
    template_name = 'index-list-right.html'
class Postdetails1View(TemplateView):
    template_name = 'post-details-1.html'
class Postdetails2View(TemplateView):
    template_name = 'post-details-2.html'
class PostelementsView(TemplateView):
    template_name = 'post-elements.html'
class PrivacypolicyView(TemplateView):
    template_name = 'privacy-policy.html'
class TermsconditionsView(TemplateView):
    template_name = 'terms-conditions.html'