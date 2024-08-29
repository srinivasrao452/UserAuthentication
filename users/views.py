
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from users.forms import UserRegistrationForm

from django.contrib.auth import logout
from django.contrib import messages


def home_view(request):
    context = {
        "user" : request.user
    }
    return render(request, 'users/home.html', context)

def contact_view(request):
    context = {
        "data" : "Please contact the admin people for more information"
    }
    return render(request, 'users/contact.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')
    # return redirect('home_page')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) # {"username" : "..", "email" : "...", ....}
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            # username = form.cleaned_data.get('username')
            messages.success(request, f"{username} Account Created Successfully")
            return redirect('login_page')

            # context = {
            #     "message" : "Registration done successfully!"
            # }
            # return render(request, 'users/register.html', context)
        else:
            username = request.POST.get('username')
            messages.warning(request, f"{username} Account Not Created successfully")
            return redirect('register_page')

            # context = {
            #     "error" : "Registration form is invalid"
            # }
            # return render(request, 'users/register.html', context)

    else:
        form = UserRegistrationForm()
        context = {
            "form" : form
        }
        return render(request, 'users/register.html', context)
















