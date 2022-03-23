from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .profile.views import ProfileView, image_upload_ajax, user_site

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('account/profile/<user>/image/', image_upload_ajax, name='image_upload'),
    path('account/profile/<user>/user_site/', user_site, name='user_site'),
    path('account/profile/<user>', ProfileView.as_view(), name='user-profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
