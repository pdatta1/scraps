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
    path('edit_post/<int:pk>', views.PostUpdateView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', views.PostDeleteView.as_view(), name='delete_post'),
    path('succeed_edit_post', views.succeed_edit_post, name='succeed_edited'),
    path('logout', views.logout_user, name='logout'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
