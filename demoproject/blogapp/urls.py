from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView


app_name = 'blogapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    # path('send-from-email/', views.SendFormEmail.as_view(), name='sendemail'),
    path('contact/', views.contact, name='contact'),
    path('create', views.PostCreateView.as_view(), name='create'),
    path('thanks', views.thanks, name='thanks'),
    path('search', views.search, name='search'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
    path('comment/<int:pk>', views.CommentCreateView.as_view(), name='comment'),
    path("comment_delete/<int:post_id>/<int:pk>", views.CommentDeleteView.as_view(), name='comment-delete'),
    path("userdashboard/", views.userdashboard, name='userdashboard'),
    path("profile/<int:pk>", views.ProfileUpdateView.as_view(), name='profile'),
    path('user_dashboard', views.signup, name='user_dashboard'),
    path('detail/<int:pk>', views.detail, name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
