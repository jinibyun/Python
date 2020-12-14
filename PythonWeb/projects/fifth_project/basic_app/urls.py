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
    path('list/', views.SchoolListView.as_view(), name ="list"),
    path('list/<int:pk>/', views.SchoolDetailView.as_view(), name ="detail"),
    path('create/', views.SchoolCreateView.as_view(), name ="create"),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name ="update"),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name ="delete"),
]