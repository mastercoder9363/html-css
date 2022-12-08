from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexx),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view())
]
