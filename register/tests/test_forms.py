from django.test import TestCase
from register.forms import RegisterForm

class RegisterFormTest(TestCase):
    
    def test_form_valid_data(self):
        form = RegisterForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@umass.edu',
            'password1': 'thispassword',
            'password2': 'thispassword',
        })

        self.assertTrue(form.is_valid())

    def test_form_invalid_email(self):
        form = RegisterForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@gmail.com',  # not a umass.edu address
            'password1': 'thispassword',
            'password2': 'thispassword',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['email'], ['Must be a @umass.edu address'])

    def test_form_password_mismatch(self):
        form = RegisterForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@umass.edu',
            'password1': 'thispassword',
            'password2': 'wrongpassword',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['password2'], ["The two password fields didn’t match."])
