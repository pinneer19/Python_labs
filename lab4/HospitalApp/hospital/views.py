from django.shortcuts import render, redirect
from .forms import SignUpForm


def index(request):
    return render(request, 'hospital/index.html')


def contact(request):
    return render(request, 'hospital/contact.html')


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    data = {
        'form': form
    }
    return render(request, 'hospital/signup.html', data)