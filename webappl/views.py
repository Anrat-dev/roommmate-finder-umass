from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from webappl.models import Profile

def home_page(request):
    return render(request, 'webappl/home_page.html', {})

def profile_page(request):
    current_user = request.user
    p = Profile.objects.get(userid=current_user)

    # print current_user.id
    return render(request, 'webappl/profile_page.html', {'current_user':current_user,
                                                         'phno':p.phno,
                                                         'gender':p.get_gender_display(),
                                                         'level_of_study':p.get_level_of_study_display(),
                                                         'year':p.get_year_display(), 
                                                         'college':p.get_college_display(),
                                                         'program':p.get_program_display(),
                                                         'sleep_habit':p.get_sleep_habit_display(),
                                                         'cleanliness':p.get_cleanliness_display(),
                                                         'social_habit':p.get_social_habit_display(),
                                                         'duration':p.get_duration_display(),
                                                         'start_season':p.get_start_season_display(),
                                                         'housing':p.get_housing_display()})