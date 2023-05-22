from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm 

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(response, new_user)
            return redirect("/edit_profile_page")
        # return redirect("/edit_profile_page")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})