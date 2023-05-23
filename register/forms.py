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

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@umass.edu" not in data:   # any check you need
            raise forms.ValidationError("Must be a @umass.edu address")
        return data

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
