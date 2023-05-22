from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from webappl.models import Profile
from views import home_page, profile_page, edit_profile_page, search_page
from forms import ProfileForm

class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            userid=self.user,
            phno='1234567890',
            gender='M',
            level_of_study='UG',
            year='1',
            college='College1',
            program='Program1',
            sleep_habit='Early',
            cleanliness='Clean',
            social_habit='Social',
            duration='1',
            start_season='Fall',
            housing='On-campus'
        )

    def test_home_page(self):
        request = self.factory.get('/')
        request.user = self.user

        response = home_page(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home Page")  # Assuming that your page has "Home Page"

    def test_profile_page(self):
        request = self.factory.get('/profile_page/')
        request.user = self.user

        response = profile_page(request)

        self.assertEqual(response.status_code, 200)
        # You can also check for user's details in the response

    def test_edit_profile_page(self):
        request = self.factory.get('/edit_profile_page/')
        request.user = self.user

        response = edit_profile_page(request)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_search_page(self):
        request = self.factory.get('/search_page/')
        request.user = self.user

        response = search_page(request)

        self.assertEqual(response.status_code, 200)
        # You can check if your scoring algorithm works by verifying that profiles are ordered as expected
