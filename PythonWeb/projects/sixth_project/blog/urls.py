from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    # base_views.py
    path('',views.index, name="index" ),
]
