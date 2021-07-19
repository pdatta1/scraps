"""scrap_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('d0oai32492384h2hdiea674t2qeyrgh2w63427/', admin.site.urls),
    path('', include('posts.urls')),
    path('s3direct/', include('s3direct.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_change/done/', auth_view.PasswordResetView.as_view(template_name='posts/password_change/password_change_done.html'), name='password_change_done'),
    path('password_change/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='posts/password_change/password_change_confirm.html'), name='password_change_confirm'),
    path('change/done', auth_view.PasswordResetCompleteView.as_view(template_name='posts/password_change_complete'), name='password_change_complete'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
