from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexx),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('author/', AuthorView.as_view()),
    path('index-full/', IndexfullView.as_view()),
    path('Indexfullleft/', IndexfullleftView.as_view()),
    path('Indexfullright/', IndexfullrightView.as_view()),
    path('Indexlist/', IndexlistView.as_view()),
]
