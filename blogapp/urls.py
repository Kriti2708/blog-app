from django.urls import path, include
from . import views


app_name = 'blogapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('create', views.PostCreateView.as_view(), name='create'),
    path('thanks', views.thanks, name='thanks'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
    path('comment', views.CommentCreateView.as_view(), name='comment'),
    path("list", views.list, name='list'),
    # path("showposts", views.showposts, name='showposts'),
    path('bloghome', views.bloghome, name='bloghome'),
    path('detail/<int:pk>', views.detail, name='post-detail')
]
