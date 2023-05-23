from django.test import TestCase
from webappl.models import Profile
from webappl.filters import ProfileForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

class ProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user1',
            email='test@example.com',
            password='testpassword'
        )

    def test_valid_form(self):
        data = {
            "phno": "1234567890",
            "profile_picture": SimpleUploadedFile("file.jpg", content=b"", content_type="image/jpeg"),
            "gender": "MALE",
            "level_of_study": "UG",
            "year": "FR",
            "college": "EDUC",
            "program": "ACC",
            "sleep_habit": "EB",
            "cleanliness": "CLEAN",
            "social_habit": "NG",
            "duration": "ONE",
            "start_season": "FALL",
            "housing": "HAVE"
        }
        form = ProfileForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            "phno": "123456789",  # This is invalid because it is not of length 10
            "profile_picture": SimpleUploadedFile("file.jpg", content=b"", content_type="image/jpeg"),
            "gender": "MALE",
            "level_of_study": "UG",
            "year": "FR",
            "college": "EDUC",
            "program": "ACC",
            "sleep_habit": "EB",
            "cleanliness": "CLEAN",
            "social_habit": "NG",
            "duration": "ONE",
            "start_season": "FALL",
            "housing": "HAVE"
        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())
