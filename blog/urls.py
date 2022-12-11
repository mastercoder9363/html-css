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
    path('indexfullleft/', IndexfullleftView.as_view()),
    path('indexfullright/', IndexfullrightView.as_view()),
    path('indexlist/', IndexlistView.as_view()),
    path('indexlistleft/', IndexlistleftView.as_view()),
    path('indexlistright/', IndexlistrightView.as_view()),
    path('postdetails1/', Postdetails1View.as_view()),
    path('postdetails2/', Postdetails2View.as_view()),
    path('postelements/', PostelementsView.as_view()),
    path('privacypolicy/', PrivacypolicyView.as_view()),
    path('termsconditions/', TermsconditionsView.as_view())
]
