from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

projects = [
    {
        "name": "Project 1",
        "description": "Project description",
        "logs": [
             {
               'author': 'User1',
               'title': 'Log-1',
               'content': 'First log content',
               'date_posted': 'May 18,2020'
             },
             {
               'author': 'User2',
               'title': 'Log-2',
               'content': 'Second log content',
               'date_posted': 'May 19,2020'
             }

        ]

        },
        {
        "name": "Project 2",
        "description": "Project description",
        "logs": [
             {
               'author': 'User1',
               'title': 'Log-1',
               'content': 'First log content',
               'date_posted': 'May 18,2020'
             },
             {
               'author': 'User2',
               'title': 'Log-2',
               'content': 'Second log content',
               'date_posted': 'May 19,2020'
             }

        ]

        }
]

  



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('user/profile-edit')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
##        b_form = BioUpdateForm(request.POST, request.FILES, instace=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
##            b_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-edit')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
##        b_form = BioUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
##        'b_form':b_form
    }

    return render(request, 'user/profile-edit.html', context)


def homepage(request):
    context = {
        'projects': projects
    }

    return render(request, 'user/homepage.html', context)


def newlog(request):
    return render(request, 'user/newlog.html')
