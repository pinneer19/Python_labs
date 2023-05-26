from datetime import datetime, timedelta, timezone

import requests
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from service.models import Service, ServiceCategory
from service.forms import ServiceForm
from doctor.models import Doctor
from client.models import Client, Passport
from doctor.forms import DoctorSignUpForm

from client.forms import ClientSignUpForm, PassportForm


def index(request):
    api_key = 'at_0sitq5Xogpxhk2Sdt4n6ulMUdumrw'
    url_ip = 'https://api64.ipify.org/?format=json'
    ip = requests.get(url_ip).json()['ip']

    url = f'https://geo.ipify.org/api/v2/country?apiKey={api_key}&ipAddress={ip}'
    offset = requests.get(url.format(ip)).json()['location']['timezone']

    hours, minutes = map(int, offset.split(':'))

    tz = timezone(timedelta(hours=hours, minutes=minutes))

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
    data = {
        'timezone': tz,
        'datetime': datetime.now(tz),
        'categories': categories,
        'services': services,
        'price_range': price_range,
    }

    return render(request, 'hospital/index.html', data)


def contact(request):
    return render(request, 'hospital/contact.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')


def delete_item(request, item_type, item_id):
    if item_type == 'service':
        service = Service.objects.get(pk=item_id)
        service.delete()
        return redirect('/main/?show_services=true')
    elif item_type == 'doctor':
        doctor = Doctor.objects.get(pk=item_id)
        doctor.delete()
        return redirect('/main/?show_doctors=true')
    elif item_type == 'client':
        client = Client.objects.get(pk=item_id)
        client.delete()
        return redirect('/main/?show_clients=true')


def edit_item(request, item_type, item_id1, item_id2=None):
    if item_type == 'service':
        service = Service.objects.get(pk=item_id1)

        if request.method == 'POST':
            form = ServiceForm(request.POST, instance=service)
            if form.is_valid():
                form.save()
                return redirect('/main/?show_services=true')
        else:
            form = ServiceForm(instance=service)

        return render(request, 'hospital/edit_item.html',
                      {'form': form, 'edit_title': 'Редактирование услуги', 'url_show': 'show_services'})
    elif item_type == 'doctor':

        doctor = Doctor.objects.get(pk=item_id1)

        if request.method == 'POST':
            form = DoctorSignUpForm(request.POST, instance=doctor)

            if form.is_valid():
                form.save()
                return redirect('/main/?show_doctors=true')
        else:
            print(doctor.password)
            form = DoctorSignUpForm(instance=doctor)

        return render(request, 'hospital/edit_item.html',
                      {'form': form, 'edit_title': 'Редактирование врача', 'url_show': 'show_doctors'})

    elif item_type == 'client':

        client = Client.objects.get(pk=item_id1)
        passport = Passport.objects.get(pk=item_id2)
        if request.method == 'POST':
            form = ClientSignUpForm(request.POST, instance=client)
            passport_form = PassportForm(request.POST, instance=passport)

            if form.is_valid() and passport_form.is_valid():
                passport = passport_form.save()
                client = form.save(commit=False)
                client.passport = passport
                client.save()

                return redirect('/main/?show_clients=true')
        else:
            form = ClientSignUpForm(instance=client)
            passport_form = PassportForm(instance=passport)
            print(client.password)
        return render(request, 'hospital/edit_item.html',
                      {'form': form, 'passport_form': passport_form, 'edit_title': 'Редактирование клиента',
                       'url_show': 'show_clients'})

    return redirect('/main')  # or return an error response


def main(request):
    show_doctors = request.GET.get('show_doctors')
    show_clients = request.GET.get('show_clients')
    show_services = request.GET.get('show_services')
    show_visits = request.GET.get('show_visits')

    services = Service.objects.all()
    doctors = Doctor.objects.all()
    clients = Client.objects.all()
    return render(request, 'hospital/main.html',
                  {'show_doctors': show_doctors, 'show_clients': show_clients, 'show_visits': show_visits,
                   'show_services': show_services, 'services': services, 'doctors': doctors, 'clients': clients})


def add_item(request, item_type):
    if item_type == 'service':
        if request.method == 'POST':
            form = ServiceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/main/?show_services=true')
        else:
            form = ServiceForm()

        return render(request, 'hospital/add_item.html',
                      {'form': form, 'add_title': 'Добавление услуги', 'url_show': 'show_services'})
    elif item_type == 'doctor':
        if request.method == 'POST':
            form = DoctorSignUpForm(request.POST)
            if form.is_valid():
                doctor = form.save(commit=False)

                user = User.objects.create_user(
                    username=doctor.login,
                    password=doctor.password
                )

                group = Group.objects.get(name='doctor')
                group.user_set.add(user)

                doctor.user = user
                doctor.save()

                return redirect('/main/?show_doctors=true')
        else:
            form = DoctorSignUpForm()

        return render(request, 'hospital/add_item.html',
                      {'form': form, 'add_title': 'Добавление врача', 'url_show': 'show_doctors'})
    elif item_type == 'client':
        if request.method == 'POST':
            form = ClientSignUpForm(request.POST)
            passport_form = PassportForm(request.POST)

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

                return redirect('/main/?show_clients=true')
        else:
            form = ClientSignUpForm()
            passport_form = PassportForm()

            return render(request, 'hospital/add_item.html',
                          {'form': form, 'passport_form': passport_form, 'add_title': 'Добавление клиента',
                           'url_show': 'show_clients'})


def info(request):
    user = request.user
    if user.is_superuser:
        return redirect('/main')
    elif user.groups.filter(name='client').exists():
        return redirect('/client/info')
    else:
        return redirect('/doctor/info')
