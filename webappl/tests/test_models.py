from django.test import TestCase
from django.contrib.auth.models import User
from webappl.models import Profile, Request

class ModelsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1',
            email='test1@example.com',
            password='testpassword1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpassword2'
        )

        self.profile1 = Profile.objects.create(
            userid=self.user1,
            phno='1234567890',
            profile_picture=None,
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

        self.profile2 = Profile.objects.create(
            userid=self.user2,
            phno='0987654321',
            profile_picture=None,
            gender='FEMALE',
            level_of_study='GA',
            year='PHD',
            college='ENG',
            program='CS',
            sleep_habit='NO',
            cleanliness='DIRTY',
            social_habit='YG',
            duration='FOUR',
            start_season='SUMMER',
            housing='NEED'
        )

        self.request = Request.objects.create(
            requesterid=self.user1,
            recipientid=self.user2,
            status='pending'
        )

    def test_profile_creation(self):
        self.assertIsInstance(self.profile1, Profile)
        self.assertIsInstance(self.profile2, Profile)

    def test_profile_str(self):
        self.assertEqual(str(self.profile1), self.user1.username)
        self.assertEqual(str(self.profile2), self.user2.username)

    def test_request_creation(self):
        self.assertIsInstance(self.request, Request)

    def test_request_str(self):
        expected_string = f"requester: {self.request.requesterid}, recipient: {self.request.recipientid}, status: {self.request.status}"
        self.assertEqual(str(self.request), expected_string)
