from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ClientSignUpForm, LoginForm, DoctorSignUpForm, PassportForm
from django.contrib.auth import logout, authenticate, get_user_model
from doctor.models import Doctor

def index(request):
    return render(request, 'hospital/index.html')


def contact(request):
    return render(request, 'hospital/contact.html')


def signup(request):
    return render(request, 'hospital/signup.html')


User = get_user_model()


def register_client(request):
    form = ClientSignUpForm(request.POST or None)
    passport_form = PassportForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid() and passport_form.is_valid():
            passport = passport_form.save()
            client = form.save(commit=False)
            client.passport = passport

            user = User.objects.create_user(
                username=passport.serial + passport.number,
                password=form.cleaned_data['password']
            )
            client.user = user
            client.save()

            return redirect('/login/')
        else:
            print(form.errors)
    data = {
        'form': form,
        'passport_form': passport_form
    }
    return render(request, 'hospital/signup_client.html', data)


def register_doctor(request):
    form = DoctorSignUpForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            client = form.save(commit=False)
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            client.user = user
            user.save()

            return redirect('/login/')
        else:
            print(form.errors)

    data = {
        'form': form
    }
    return render(request, 'hospital/signup_doctor.html', data)


def logout_user(request):
    logout(request)
    return redirect('/login/')
