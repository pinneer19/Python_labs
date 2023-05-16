from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import Group
from .forms import DoctorSignUpForm

User = get_user_model()


def register_doctor(request):
    form = DoctorSignUpForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            client = form.save(commit=False)
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )

            group = Group.objects.get(name='doctor')
            group.user_set.add(user)
            client.user = user

            user.save()

            return redirect('/login/')
        else:
            print(form.errors)

    data = {
        'form': form
    }
    return render(request, 'doctor/signup_doctor.html', data)


def info(request):
    return render(request, 'doctor/info.html')
