from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('profile', views.my_profile, name='profile'),
    path('create_post', views.create_post, name='create_post'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),


]
