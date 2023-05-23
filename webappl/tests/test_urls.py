from django.test import TestCase, Client
from django.urls import reverse, resolve
from . import views

class URLTests(TestCase):
    def setUp(self):
        self.client = Client()

    # Unit tests
    def test_url_resolves_correct_view(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func, views.home_page)

        url = reverse('profile_page')
        self.assertEquals(resolve(url).func, views.profile_page)

        url = reverse('edit_profile_page')
        self.assertEquals(resolve(url).func, views.edit_profile_page)

        url = reverse('search_page')
        self.assertEquals(resolve(url).func, views.search_page)

    # # Integration tests
    def test_url_returns_correct_html(self):
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertContains(response, '<h1>Home Page</h1>') # Assuming that your page has <h1>Home Page</h1>

        url = reverse('profile_page')
        response = self.client.get(url)
        self.assertContains(response, '<h1>Profile Page</h1>') # Assuming that your page has <h1>Profile Page</h1>

        url = reverse('edit_profile_page')
        response = self.client.get(url)
        self.assertContains(response, '<h1>Edit Profile Page</h1>') # Assuming that your page has <h1>Edit Profile Page</h1>

        url = reverse('search_page')
        response = self.client.get(url)
        self.assertContains(response, '<h1>Search Page</h1>') # Assuming that your page has <h1>Search Page</h1>

    # Functional tests
    def test_url_returns_correct_status_code(self):
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('profile_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('edit_profile_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('search_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
