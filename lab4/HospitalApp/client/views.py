from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render, reverse, redirect
from .forms import ClientSignUpForm, PassportForm

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

            group = Group.objects.get(name='client')
            group.user_set.add(user)

            client.user = user
            client.save()

            # return redirect('/login/')
            return redirect(reverse('hospital:login'))
        else:
            print(form.errors)
    data = {
        'form': form,
        'passport_form': passport_form
    }
    return render(request, 'client/signup_client.html', data)


def info(request):
    return render(request, 'client/info.html')
