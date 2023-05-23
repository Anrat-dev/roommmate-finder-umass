from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile, Request
import tempfile


class ProfileTestCase(TestCase):
    def setUp(self):
        # Create a temporary image file
        tmp_image = tempfile.NamedTemporaryFile(suffix=".jpg").name

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create a test profile
        self.profile = Profile.objects.create(
            userid=self.user,
            phno='1234567890',
            profile_picture=tmp_image,
            gender='MALE',
            level_of_study='UG',
            year='FR',
            college='EDUC',
            program='ACC',
            sleep_habit='EB',
            cleanliness='CLEAN',
            social_habit='NG',
            duration='ONE',
            start_season='FALL',
            housing='HAVE'
        )

    def test_profile_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(self.profile.__str__(), self.profile.userid.username)

    def test_profile_update(self):
        self.profile.gender = 'FEMALE'
        self.profile.save()
        self.assertEqual(Profile.objects.get(userid=self.user).gender, 'FEMALE')

    def test_profile_delete(self):
        self.profile.delete()
        self.assertEqual(Profile.objects.filter(userid=self.user).count(), 0)


class RequestTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')

        self.request = Request.objects.create(
            requesterid=self.user1,
            recipientid=self.user2,
            status='pending'
        )

    def test_request_creation(self):
        self.assertTrue(isinstance(self.request, Request))
        self.assertEqual(self.request.__str__(), f"requester: {self.request.requesterid}, recipient: {self.request.recipientid}, status: {self.request.status}")

    def test_request_update(self):
        self.request.status = 'accepted'
        self.request.save()
        self.assertEqual(Request.objects.get(requesterid=self.user1, recipientid=self.user2).status, 'accepted')

    def test_request_delete(self):
        self.request.delete()
        self.assertEqual(Request.objects.filter(requesterid=self.user1, recipientid=self.user2).count(), 0)
