from django.conf.urls import  url
from django.urls import path

from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register, name="register" ),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
]