from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('profile', views.my_profile, name='profile'),
    path('create_post', views.create_post, name='create_post'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login_user, name='login'),
    path('password_change', views.change_password, name='change_password'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('posts/edit_post/<int:pk>', views.PostUpdateView.as_view(), name='edit_post'),
    path('edit_user', views.edit_profile, name='edit_user'),
    path('post/view_profile/<int:pk>', views.View_Profile.as_view(), name='view_profile'),
    path('edit_profile', views.edit_profilepic, name='edit_profilepic'),   
    path('posts/delete_post/<int:pk>', views.PostDeleteView.as_view(), name='delete_post'),
    path('succeed_edit_post', views.succeed_edit_post, name='succeed_edited'),
    path('pump_detail/<int:pk>', views.pump, name='pumped_detail'),
    path('logout', views.logout_user, name='logout'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),


]
