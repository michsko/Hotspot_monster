from django.urls import path
from . import views 


urlpatterns = [

path('', views.index, name='index'),
path('404', views.fournullfour, name='fournullfour'),
path('about', views.about, name='about'),
path('blog_grid', views.blog_grid, name='blog_grid'),
path('blog_single', views.blog_single, name='blog_single'),
path('blog_standard', views.blog_standard, name='blog_standard'),
path('contact', views.contact, name='contact'),

]
