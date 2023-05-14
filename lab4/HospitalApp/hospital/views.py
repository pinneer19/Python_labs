from datetime import datetime, timedelta, timezone

import requests
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def index(request):
    api_key = 'at_0sitq5Xogpxhk2Sdt4n6ulMUdumrw'
    url_ip = 'https://api64.ipify.org/?format=json'
    ip = requests.get(url_ip).json()['ip']

    url = f'https://geo.ipify.org/api/v2/country?apiKey={api_key}&ipAddress={ip}'
    offset = requests.get(url.format(ip)).json()['location']['timezone']

    hours, minutes = map(int, offset.split(':'))

    tz = timezone(timedelta(hours=hours, minutes=minutes))

    data = {
        'timezone': tz,
        'datetime': datetime.now(tz)
    }
    return render(request, 'hospital/index.html', data)


def contact(request):
    return render(request, 'hospital/contact.html')


def signup(request):
    return render(request, 'hospital/signup.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')
