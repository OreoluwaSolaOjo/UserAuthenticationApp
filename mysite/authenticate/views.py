from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm

# Create your views here.


def home(request):
    return render(request, 'authenticate/home.html')


def login_user(request):
    if request.method == "POST":
        # If username and password is post username and password, put into the username and password variable
        username = request.POST['username']
        password = request.POST['password']
        # create user object and authenticate to check
        user = authenticate(request, username=username, password=password)
        #  if the user object exists then
        if user is not None:
            login(request, user)
            # success message
            messages.success(request, ('You have logged in successfully'))
            # redirect to the next page
            return redirect('home')
        else:
            messages.success(request, ('Error Logging in, Please try again!!'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been Logged out'))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        # Taking the information POSTED into UserCreationForm and putting it into a variable form
        form = SignUpForm(request.POST)
        # Check if form is valid and save into the database
        if form.is_valid():
            form.save()
            # pass the user info into authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            # print message
            messages.success(request, ('You have been registered'))
            return redirect('home')

    else:
        form = SignUpForm()
    # passing the form into the context variable which represents a dictionary
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


def edit_profile(request):
    if request.method == "POST":
        # Taking the information POSTED into UserCreationForm and putting it into a variable form
        # The instance passes in the user info that is in the database
        form = EditProfileForm(request.POST, instance=request.user)
        # Check if form is valid and save into the database
        if form.is_valid():
            form.save()
            # print message
            messages.success(request, ('You have Edited your profile'))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)
    # passing the form into the context variable which represents a dictionary
    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)


def change_password(request):
    if request.method == "POST":
        # Taking the information POSTED into UserCreationForm and putting it into a variable form
        # The instance passes in the user info that is in the database
        form = PasswordChangeForm(data=request.POST, user=request.user)
        # Check if form is valid and save into the database
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # print message
            messages.success(request, ('You have Edited your password'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    # passing the form into the context variable which represents a dictionary
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)
