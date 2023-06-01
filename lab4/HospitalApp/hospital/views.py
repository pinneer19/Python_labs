import json
from datetime import datetime, timedelta, timezone

import requests
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from order.models import Order, OrderService
from service.models import Service, ServiceCategory
from service.forms import ServiceForm
from doctor.models import Doctor
from client.models import Client, Passport
from doctor.forms import DoctorSignUpForm
from order.forms import OrderForm, OrderServiceForm
from client.forms import ClientSignUpForm, PassportForm
from visit.models import Visit


def index(request):
    api_key = 'at_0sitq5Xogpxhk2Sdt4n6ulMUdumrw'
    url_ip = 'https://api64.ipify.org/?format=json'
    ip = requests.get(url_ip).json()['ip']

    url = f'https://geo.ipify.org/api/v2/country?apiKey={api_key}&ipAddress={ip}'
    offset = requests.get(url.format(ip)).json()['location']['timezone']

    hours, minutes = map(int, offset.split(':'))

    tz = timezone(timedelta(hours=hours, minutes=minutes))

    start_price = request.GET.get('start_price')
    end_price = request.GET.get('end_price')

    if start_price and end_price:
        start_price = float(start_price)
        end_price = float(end_price)
        services = Service.objects.filter(price__gte=start_price, price__lte=end_price)
    else:
        services = Service.objects.all()

    categories = ServiceCategory.objects.all()
    selected_category = request.GET.get('category')
    category = None
    if selected_category:
        services = services.filter(category_id=selected_category)
        category = categories.get(id=selected_category)

    data = {
        'timezone': tz,
        'datetime': datetime.now(tz),
        'categories': categories,
        'services': services,
        'start_price': start_price,
        'end_price': end_price,
        'selected_category': selected_category,
        'category_by_id': category
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
    elif item_type == 'order':
        order = Order.objects.get(pk=item_id)
        order.delete()
        return redirect('/main/?show_orders=true')


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

        return render(request, 'hospital/edit_item.html',
                      {'form': form, 'passport_form': passport_form, 'edit_title': 'Редактирование клиента',
                       'url_show': 'show_clients'})
    elif item_type == 'order':

        order = Order.objects.get(pk=item_id1)
        order_data = []
        order_services = OrderService.objects.all()
        for order_service in order_services:
            if order_service.order == order:
                order_data.append(order_service.service.name)

        if request.method == 'POST':
            order_form = OrderForm(request.POST, instance=order)

            if order_form.is_valid():
                order = order_form.save()
                order_form_data = model_to_dict(order)
                order_form_data['date'] = order.date.strftime('%Y-%m-%d')

                order_json = json.dumps(order_form_data)

                request.session['order'] = order_json
                request.session['services'] = order_data
                return redirect('/add/order/services/')

        else:
            order_form = OrderForm(instance=order)

        return render(request, 'hospital/add_item.html',
                      {'form': order_form, 'add_title': 'Изменение заказа',
                       'url_show': 'show_orders'})

    return redirect('/main')  # or return an error response


def main(request):
    show_doctors = request.GET.get('show_doctors')
    show_clients = request.GET.get('show_clients')
    show_services = request.GET.get('show_services')
    show_orders = request.GET.get('show_orders')
    show_planned_visits = request.GET.get('planned_visits')
    show_visits = request.GET.get('show_visits')
    show_result = request.GET.get('show_result')
    sort_by_date = request.GET.get('sort_by_date')
    show_patients = request.GET.get('show_patients')
    services = Service.objects.all()
    doctors = Doctor.objects.all()
    clients = Client.objects.all()
    orders = Order.objects.all()
    selected_client = request.GET.get('client')

    if selected_client:
        order_services = OrderService.objects.filter(order__client_id=selected_client)
    else:
        order_services = OrderService.objects.all()

    if sort_by_date == 'true':
        order_services = order_services.order_by('date')

    order_data = {}  # Dictionary to store order data

    for order in orders:
        data = []
        for order_service in order_services:
            if order_service.order == order:
                data.append(order_service.service.name)

        order_data[order.id] = data  # Store the data for each order in the dictionary

    total_cost = 0.0
    if show_result:
        client = request.GET.get('client')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        doctor = request.GET.get('doctor')

        if client and start_date and end_date and doctor:
            visits_date_range = Visit.objects.filter(visit_date__range=[start_date, end_date])
            client_visits_for_doctor = visits_date_range.filter(client=client, doctor=doctor)

            for visit in client_visits_for_doctor:
                total_cost += visit.service.price

    patients_list = []
    if show_patients:
        selected_doctor = request.GET.get('doctor')
        print(selected_doctor)
        if selected_doctor:
            order_services_patients = set(
                order_service.order.client for order_service in order_services if selected_doctor == order_service.doctor)
            visits_patients = set(visit.client for visit in Visit.objects.filter(doctor=selected_doctor))

            patients_list = order_services_patients.union(visits_patients)

    return render(request, 'hospital/main.html',
                  {'show_doctors': show_doctors, 'show_clients': show_clients, 'show_orders': show_orders,
                   'show_services': show_services, 'services': services, 'doctors': doctors, 'clients': clients,
                   'orders': orders, 'order_data': order_data, 'order_services': order_services,
                   'planned_visits': show_planned_visits, 'sort_by_date': sort_by_date,
                   'selected_client': selected_client, 'show_visits': show_visits, 'total_cost': total_cost,
                   'show_result': show_result, 'show_patients': show_patients, 'patients_list': patients_list})


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
    elif item_type == 'order':
        if request.method == 'POST':
            order_form = OrderForm(request.POST)

            if order_form.is_valid():
                order = order_form.save()
                order_data = model_to_dict(order)
                order_data['date'] = order.date.strftime('%Y-%m-%d')
                order_json = json.dumps(order_data)

                # Store the order JSON in the session
                request.session['order'] = order_json
                return redirect('services/')

        else:
            order_form = OrderForm()

        return render(request, 'hospital/add_item.html',
                      {'form': order_form, 'add_title': 'Добавление заказа',
                       'url_show': 'show_orders'})
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


def add_services_to_order(request):
    order = request.session.get('order')
    services = request.session.get('services', None)

    if request.method == 'POST':

        order_service_form = OrderServiceForm(request.POST)

        if order_service_form.is_valid():
            order_service = order_service_form.save(commit=False)

            json_data = json.loads(order)
            order_service.order = Order(client=Client.objects.get(id=json_data['client']), date=json_data['date'],
                                        id=json_data['id'])
            order_service.save()

            del request.session['order']

            return redirect('/main/?show_orders=true')
    else:
        order_service_form = OrderServiceForm()

    return render(request, 'hospital/add_item.html',
                  {'form': order_service_form, 'services': services, 'add_title': 'Добавление услуги',
                   'url_show': 'show_orders'})
