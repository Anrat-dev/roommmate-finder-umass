from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import home_page, profile_page, edit_profile_page, search_page, contacts, accept_contact, search

class TestUrls(SimpleTestCase):

    def test_home_page_url(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func, home_page)

    def test_profile_page_url(self):
        url = reverse('profile_page')
        self.assertEquals(resolve(url).func, profile_page)

    def test_profile_page_with_pk_url(self):
        url = reverse('profile_page_with_pk', args=['1'])
        self.assertEquals(resolve(url).func, profile_page)

    def test_edit_profile_page_url(self):
        url = reverse('edit_profile_page')
        self.assertEquals(resolve(url).func, edit_profile_page)

    def test_search_page_url(self):
        url = reverse('search_page')
        self.assertEquals(resolve(url).func, search_page)

    def test_contacts_url(self):
        url = reverse('contacts')
        self.assertEquals(resolve(url).func, contacts)

    def test_contacts_with_pk_url(self):
        url = reverse('contacts_with_pk', args=['1'])
        self.assertEquals(resolve(url).func, contacts)

    def test_search_url(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

