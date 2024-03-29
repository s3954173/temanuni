"""
URL configuration for temanuni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views as home_views
from users import views as user_views
from events import views as events_views
from tmProfile import views as profile_views
from mfa import views as mfa_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('events/', events_views.events, name='events'),
    path('create_event_user/', events_views.create_event_user, name='create_event_user'),
    path('profile/', profile_views.profile, name='profile'),
    path('mfa/', mfa_views.mfa, name='mfa'),
    path('verify/', mfa_views.verify, name='verify'),
]
