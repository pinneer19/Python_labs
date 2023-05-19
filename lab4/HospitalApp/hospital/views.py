from datetime import datetime, timedelta, timezone

import requests
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from service.models import Service, ServiceCategory
from service.forms import ServiceForm
from doctor.models import Doctor
from client.models import Client


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


def delete_service(request, item_id):
    item = Service.objects.get(pk=item_id)
    item.delete()
    return redirect('/main/?show_services=true')


def edit_item(request, item_type, item_id):
    if item_type == 'service':
        service = Service.objects.get(pk=item_id)

        if request.method == 'POST':
            form = ServiceForm(request.POST, instance=service)
            if form.is_valid():
                form.save()
                return redirect('/main/?show_services=true')
        else:
            form = ServiceForm(instance=service)

        return render(request, 'hospital/edit_service.html', {'form': form})

    # Handle other item types if needed
    # ...

    # Return an error or redirect to an appropriate page
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

        return render(request, 'hospital/add_service.html', {'form': form})


def info(request):
    user = request.user
    if user.is_superuser:
        return redirect('/main')
    elif user.groups.filter(name='client').exists():
        return redirect('/client/info')
    else:
        return redirect('/doctor/info')
