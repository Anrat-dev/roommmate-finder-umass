from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["phno", "profile_picture", "gender", "level_of_study", "year", "college", "program", "sleep_habit", "cleanliness", "social_habit", "duration", "start_season", "housing"]