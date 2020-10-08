from django.urls import path, include

from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    # 1. function view
    # path('', views.index, name="index"), # '/' path

    # 2. class view
    # path('', views.CBView.as_view(), name="index"), # '/' path

    # 3. template view
    path('', views.IndexView.as_view(), name="index"), # '/' path
]