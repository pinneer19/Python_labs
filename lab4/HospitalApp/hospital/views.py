from datetime import datetime, timedelta, timezone

import requests
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from service.models import Service, ServiceCategory


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

    user = request.user

    if user.is_superuser:
        return render(request, 'hospital/main.html', context)
    elif user.groups.filter(name='client').exists():
        return redirect('/client/info')
    else:
        return redirect('/doctor/info')

