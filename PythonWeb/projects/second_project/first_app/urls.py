
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('formpage/',views.form_name_view, name="formpage" ),
    path('newformpage/',views.users, name="newformpage" ),
]