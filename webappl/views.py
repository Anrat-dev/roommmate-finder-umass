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
                                                         'gender':p.gender,
                                                         'level_of_study':p.level_of_study,
                                                         'year':p.year, 
                                                         'college':p.college,
                                                         'program':p.program,
                                                         'sleep_habit':p.sleep_habit,
                                                         'cleanliness':p.cleanliness,
                                                         'social_habit':p.social_habit,
                                                         'duration':p.duration,
                                                         'start_season':p.start_season,
                                                         'housing':p.housing})