from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ClientSignUpForm, LoginForm, DoctorSignUpForm, PassportForm
from django.contrib.auth import logout
from django.utils.translation import activate


def index(request):
    return render(request, 'hospital/index.html')


def login(request):
    # if request.method == 'GET':
    #     context = ''
    #     return render(request, 'mytest/login.html', {'context': context})
    #
    # elif request.method == 'POST':
    #     username = request.POST.get('username', '')
    #     password = request.POST.get('password', '')
    #
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         # Redirect to a success page?
    #         # return HttpResponseRedirect('/')
    #     else:
    #         context = {'error': 'Wrong credintials'}  # to display error?
    #         return render(request, 'mytest/login.html', {'context': context})


    return render(request, 'hospital/login.html')

def contact(request):
    return render(request, 'hospital/contact.html')


def signup(request):
    return render(request, 'hospital/signup.html')


def register_client(request):

    form = ClientSignUpForm(request.POST or None)
    passport_form = PassportForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid() and passport_form.is_valid():
            passport = passport_form.save()
            client = form.save(commit=False)
            client.passport = passport
            client.save()

            return redirect('/login/')


    data = {
        'form': form,
        'passport_form': passport_form
    }
    return render(request, 'hospital/signup_client.html', data)


def register_doctor(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        print(form.data)

        print(form.cleaned_data['department'])
        # form.department = request.REQUEST.get('department')
        if form.is_valid():
            form.save()
            print("OK")
            user = User.objects.create_user(username=request.REQUEST.get('login', None),
                                            password=request.REQUEST.get('password', None))
            user.save()

            return redirect('/login/')
        else:
            print("Errors")
            print(dir(form))
            print(form.errors)

    else:
        form = DoctorSignUpForm()

    data = {
        'form': form
    }
    return render(request, 'hospital/signup_doctor.html', data)


def logout_user(request):
    logout(request)
    return redirect('/login/')
