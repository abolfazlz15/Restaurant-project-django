from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


def registerView(request):
    if request.user.is_authenticated:  # The logged in user does not have access to the login page
        return redirect('blog:article_list')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')
    else:
        form = RegisterForm()


    return render(request, 'account/register.html', context={'form': form})

def loginView(request):
    if request.user.is_authenticated:  # The logged in user does not have access to the login page
        return redirect('blog:article_list')
    # for login
    if request.method == 'POST':
        print('test')
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('blog:article_list')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', context={'form': form})


def editProfile(request):
    if not request.user.is_authenticated:  # The logged in user does not have access to the login page
        return redirect('account:login')
    if request.method == 'POST':
        form = EditProfileForm(instance=request.user, data=request.POST)
        if form.is_valid:
            form.save()
    form = EditProfileForm(instance=request.user)        
    return render(request, 'account/edit_profile.html', context={'form': form})

def logoutView(request):
    logout(request)
    return redirect('blog:article_list')
