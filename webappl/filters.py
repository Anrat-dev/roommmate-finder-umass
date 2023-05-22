import django_filters
from .models import Profile

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = {
            'gender': ['exact'],
            'level_of_study': ['exact'],
            'year': ['exact'],
            'college': ['exact'],
            'program': ['exact'],
            'sleep_habit': ['exact'],
            'cleanliness': ['exact'],
            'social_habit': ['exact'],
            'duration': ['exact'],
            'start_season': ['exact'],
            'housing': ['exact'],
        }