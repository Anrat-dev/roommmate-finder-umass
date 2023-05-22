import django_filters
from .models import Profile

class ProfileFilter(django_filters.FilterSet):

    class Meta:
        model = Profile
        fields = ["gender", "level_of_study", "year", "college", "program", "sleep_habit", "cleanliness", "social_habit", "duration", "start_season", "housing"]