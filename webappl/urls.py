from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile_page/', views.profile_page, name='profile_page')
]