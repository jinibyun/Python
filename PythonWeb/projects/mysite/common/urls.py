from django.urls import path
from . import views
# use "exiting" view exist in django.contrib.auth . You do not have to create another
# NOTE: it does not support html template
# error message: \mysite\templates\registration\login.html (Source does not exist)  Therefore we will have to create this template html by manual
# another way to resolve this issue is to create common/login.html and modify common/urls.py (see below)
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), # see as_view function
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'), # sign up is not supported. therefore we will have to create it
]