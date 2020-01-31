from django.urls import path
from django.views.generic.base import TemplateView
from .views import home, usersignup, usersignin, usersignout, dashboard, postArticle, showArticles

app_name = 'article'

urlpatterns = [
    path('', home, name='home'),
    path('signup', usersignup, name='signup'),
    path('login', usersignin, name='login'),
    path('logout', usersignout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('postarticle', postArticle, name='postarticle'),
    path('searcharticle', TemplateView.as_view(template_name='searchArticles.html'), name='searcharticle'),
    path('showarticles', showArticles, name='showarticles'),
]
