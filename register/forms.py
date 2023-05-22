from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # phone_no = forms.CharField(max_length=10)
    # gender = forms.ChoiceField(choices= (('M','Male'),('F','Female')('Other','Other')))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
