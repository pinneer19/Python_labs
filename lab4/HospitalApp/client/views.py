from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render, reverse, redirect
from .forms import ClientSignUpForm, PassportForm
from service.models import Service, ServiceCategory


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
            return redirect('/login/')
        else:
            print(form.errors)
    data = {
        'form': form,
        'passport_form': passport_form
    }
    return render(request, 'client/signup_client.html', data)


def info(request):
    price_range = request.GET.get('price_range', 'all')

    if price_range == 'cheap':
        services = Service.objects.order_by('price')
    elif price_range == 'expensive':
        services = Service.objects.order_by('-price')
    else:
        services = Service.objects.all()

    if price_range == 'category':
        categories = ServiceCategory.objects.order_by('name')
    else:
        categories = ServiceCategory.objects.all()

    context = {
        'categories': categories,
        'services': services,
        'price_range': price_range,
    }
    return render(request, 'client/info.html', context)
