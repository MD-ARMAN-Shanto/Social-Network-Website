from django.shortcuts import render, redirect, reverse
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid:
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html',{'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)  #data for specific password value and
                                                                        # user for specific user request
        if form.is_valid():                 # is_valid() its a self define form
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')

    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html',{'form': form})












