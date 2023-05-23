from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Profile, Request

class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home_page')
        self.profile_page_url = reverse('profile_page')
        self.edit_profile_page_url = reverse('edit_profile_page')
        self.search_page_url = reverse('search_page')


        self.test_user = User.objects.create_user(username='testuser', password='12345')
        self.test_user2 = User.objects.create_user(username='testuser2', password='12345')
        self.test_user_profile = Profile.objects.create(userid=self.test_user)
        self.test_user2_profile = Profile.objects.create(userid=self.test_user2)

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)

    def test_profile_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.profile_page_url)
        self.assertEquals(response.status_code, 200)
    
    def test_edit_profile_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.edit_profile_page_url)
        self.assertEquals(response.status_code, 200)

    def test_search_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.search_page_url)
        self.assertEquals(response.status_code, 200)


