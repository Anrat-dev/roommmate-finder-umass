from django.shortcuts import render, redirect
from filters import ProfileForm
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
from django.shortcuts import render
from django.db.models.query import QuerySet
from webappl.models import Profile, Request


from django.shortcuts import render
from .filters import ProfileFilter

def home_page(request):
    return render(request, 'webappl/home_page.html', {})

def profile_page(request, pk=None):
    if pk:
        p = Profile.objects.get(pk=pk)
        user = User.objects.get(username = p.userid.username)
        return render(request, 'webappl/profile_page.html', {'current_user':user,
                                                         'first_name':user.first_name,
                                                         'last_name':user.last_name,
                                                         'email':"*******@umass.edu",
                                                         'phno':"##########",
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
    current_user = request.user
    p = Profile.objects.get(userid=current_user)

    return render(request, 'webappl/profile_page.html', {'current_user':current_user,
                                                         'first_name':current_user.first_name,
                                                         'last_name':current_user.last_name,
                                                         'email':current_user.email,
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

def edit_profile_page(request):
    try:
        profile = request.user.profile
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid:
                form.save()
                return redirect("/profile_page")
    except:
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            form.instance.userid = request.user = request.user
            if form.is_valid:
                form.save()
                return redirect("/profile_page")
    return render(request, 'webappl/edit_profile.html', {'form':form})


def search_page(request):
    current_user = request.user
    current_profile = current_user.profile
    all_profiles = Profile.objects.all()

    # Create the filter
    profile_filter = ProfileFilter(request.GET, queryset=all_profiles.exclude(userid=current_user).exclude(userid__in=User.objects.filter(is_active=False)))

    # Apply the filter to the profiles
    filtered_profiles = profile_filter.qs

    # Get the field names of the Profile model excluding 'userid', 'phno', and 'profile_picture'
    profile_fields = [field.name for field in Profile._meta.get_fields()][2:]

    # Compute a match score for each profile excluding the current user
    scores = {}
    for profile in filtered_profiles:
        score = sum(getattr(profile, field) == getattr(current_profile, field) for field in profile_fields)
        scores[profile] = score

    # Sort the profiles based on the scores in descending order
    sorted_profiles_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    sorted_profiles = [profile for profile, _ in sorted_profiles_scores]

    return render(request, 'webappl/search_page.html', {'profiles': sorted_profiles, 'filter': profile_filter})

def contacts(request, pk=None):
    if pk:
        recipient = User.objects.get(pk=pk)
        contact_obj = Request(requesterid=request.user, recipientid=recipient, status="PENDING")
        contact_obj.save()
        return redirect("/search_page")

    contact_list = Request.objects.filter(
        Q(requesterid=request.user) | Q(recipientid=request.user)).distinct()
    return render(request, 'webappl/contacts.html', {'contact_list': contact_list})

def search(request):
    filter = ProfileFilter(request.GET, queryset=Profile.objects.all())
    return render(request, 'search.html', {'filter': filter})
