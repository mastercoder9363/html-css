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
    path('Indexfullleft/', Indexfullleft.as_view()),
]
