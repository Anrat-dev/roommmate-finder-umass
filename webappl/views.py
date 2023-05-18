from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page(request):
    return render(request, 'webappl/home_page.html', {})

def profile_page(request):
    current_user = request.user
    # print current_user.id
    return render(request, 'webappl/profile_page.html', {'current_user':current_user})