from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('edit_profile_page/', views.edit_profile_page, name='edit_profile_page'),
    path('search_page/', views.search_page, name='search_page')
]