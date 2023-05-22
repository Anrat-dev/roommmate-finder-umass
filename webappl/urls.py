from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
    url(r'^profile_page/(?P<pk>\d+)/$', views.profile_page, name='profile_page_with_pk'),
    path('edit_profile_page/', views.edit_profile_page, name='edit_profile_page'),
    path('search_page/', views.search_page, name='search_page'),
    path('contacts/', views.contacts, name='contacts'),
    url(r'^contacts/(?P<pk>\d+)/$', views.contacts, name='contacts_with_pk'),
]