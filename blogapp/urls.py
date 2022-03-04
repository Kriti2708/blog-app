from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [   
    path('', views.home, name='home'),  
    path('about', views.about, name='about'),  
    path('contact', views.contact, name='contact'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('create', views.create, name='create'),
]
