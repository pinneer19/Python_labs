import json
from datetime import datetime, timedelta, timezone, date

import requests
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.forms import model_to_dict
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseNotFound
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
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger('main')


def index(request):
    logger.info('default page loading')
    api_key = 'at_0sitq5Xogpxhk2Sdt4n6ulMUdumrw'
    url_ip = 'https://api64.ipify.org/?format=json'
    logger.info('sending API requests')
    try:

        ip = requests.get(url_ip).json()['ip']
    except requests.exceptions.ConnectionError:
        return HttpResponseBadRequest('<h1>Проверьте доступ к интернету!</h1>')
    url = f'https://geo.ipify.org/api/v2/country?apiKey={api_key}&ipAddress={ip}'

    offset = requests.get(url.format(ip)).json()['location']['timezone']

    hours, minutes = map(int, offset.split(':'))

    tz = timezone(timedelta(hours=hours, minutes=minutes))

    start_price = request.GET.get('start_price')
    end_price = request.GET.get('end_price')
    selected_category = request.GET.get('category')

    services = Service.objects.all()
    categories = ServiceCategory.objects.all()
    category_by_id = None

    if selected_category:
        services = services.filter(category_id=selected_category)
        category_by_id = categories.get(id=selected_category)

    if start_price and end_price:
        start_price = float(start_price)
        end_price = float(end_price)

        if start_price >= end_price:
            return HttpResponse('<h1>Конечная цена не может быть меньше начальной!</h1>')
        services = services.filter(price__gte=start_price, price__lte=end_price)
    elif start_price:
        start_price = float(start_price)
        services = services.filter(price__gte=start_price)
    elif end_price:
        end_price = float(end_price)
        services = services.filter(price__lte=end_price)

    data = {
        'timezone': tz,
        'datetime': datetime.now(tz),
        'categories': categories,
        'services': services,
        'start_price': start_price,
        'end_price': end_price,
        'selected_category': selected_category,
        'category_by_id': category_by_id
    }

    return render(request, 'hospital/index.html', data)


def contact(request):
    return render(request, 'hospital/contact.html')


def logout_user(request):
    logger.info('user logout')
    logout(request)
    return redirect('/login/')


@user_passes_test(lambda u: u.is_superuser)
def delete_item(request, item_type, item_id):
    logger.info(f'admin deleting item of type: {item_type}')
    if item_type == 'service':
        try:
            service = Service.objects.get(pk=item_id)
        except Service.DoesNotExist:
            logger.exception('Service.DoesNotExist')
            return HttpResponseNotFound('<h2>No such service</h2>')

        service.delete()
        return redirect('/main/?show_services=true')
    elif item_type == 'doctor':
        try:
            doctor = Doctor.objects.get(pk=item_id)
        except Doctor.DoesNotExist:
            logger.exception('Doctor.DoesNotExist')
            return HttpResponseNotFound('<h2>No such doctor</h2>')

        doctor.delete()
        return redirect('/main/?show_doctors=true')
    elif item_type == 'client':
        try:
            client = Client.objects.get(pk=item_id)
        except Client.DoesNotExist:
            logger.exception('Client.DoesNotExist')
            return HttpResponseNotFound('<h2>No such client</h2>')

        client.delete()
        return redirect('/main/?show_clients=true')
    elif item_type == 'order':
        try:
            order = Order.objects.get(pk=item_id)
        except Order.DoesNotExist:
            logger.exception('Order.DoesNotExist')
            return HttpResponseNotFound('<h2>No such order</h2>')
        order.delete()
        return redirect('/main/?show_orders=true')


@user_passes_test(lambda u: u.is_superuser)
def edit_item(request, item_type, item_id1, item_id2=None):
    logger.info(f'admin editing item of type: {item_type}')
    if item_type == 'service':
        try:
            service = Service.objects.get(pk=item_id1)
        except Service.DoesNotExist:
            logger.exception('Service.DoesNotExist')
            return HttpResponseNotFound('<h2>No such service</h2>')
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

        try:
            doctor = Doctor.objects.get(pk=item_id1)
        except Doctor.DoesNotExist:
            logger.exception('Doctor.DoesNotExist')
            return HttpResponseNotFound('<h2>No such doctor</h2>')

        if request.method == 'POST':
            form = DoctorSignUpForm(request.POST, instance=doctor)

            if form.is_valid():
                form.save()
                return redirect('/main/?show_doctors=true')
        else:
            form = DoctorSignUpForm(instance=doctor)

        return render(request, 'hospital/edit_item.html',
                      {'form': form, 'edit_title': 'Редактирование врача', 'url_show': 'show_doctors'})

    elif item_type == 'client':
        try:
            client = Client.objects.get(pk=item_id1)
        except Client.DoesNotExist:
            logger.exception('Client.DoesNotExist')
            return HttpResponseNotFound('<h2>No such client</h2>')

        try:
            passport = Passport.objects.get(pk=item_id2)
        except Passport.DoesNotExist:
            logger.exception('Passport.DoesNotExist')
            return HttpResponseNotFound('<h2>No such passport</h2>')

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


@user_passes_test(lambda u: u.is_superuser)
def main(request):
    logger.info('admin page')
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
        if selected_doctor:
            order_services_patients = set(
                order_service.order.client for order_service in order_services if
                selected_doctor == order_service.doctor)
            visits_patients = set(visit.client for visit in Visit.objects.filter(doctor=selected_doctor))

            patients_list = order_services_patients.union(visits_patients)

    return render(request, 'hospital/main.html',
                  {'show_doctors': show_doctors, 'show_clients': show_clients, 'show_orders': show_orders,
                   'show_services': show_services, 'services': services, 'doctors': doctors, 'clients': clients,
                   'orders': orders, 'order_data': order_data, 'order_services': order_services,
                   'planned_visits': show_planned_visits, 'sort_by_date': sort_by_date,
                   'selected_client': selected_client, 'show_visits': show_visits, 'total_cost': total_cost,
                   'show_result': show_result, 'show_patients': show_patients, 'patients_list': patients_list})


@user_passes_test(lambda u: u.is_superuser)
def add_item(request, item_type):
    logger.info(f'admin adding item of type: {item_type}')
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

        # specializations = Specialization.objects.all()

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
        return redirect('/main/')
    elif user.groups.filter(name='client').exists():
        return redirect('/client/info/')
    else:
        return redirect('/doctor/info/')


def home(request):
    return render(request, 'hospital/web_lab1/home.html')


def contacts(request):
    return render(request, 'hospital/web_lab1/contacts.html')


def about(request):
    return render(request, 'hospital/web_lab1/about.html')


def coupons(request):
    return render(request, 'hospital/web_lab1/coupons.html')


def dictionary(request):
    return render(request, 'hospital/web_lab1/dictionary.html')


def jobs(request):
    return render(request, 'hospital/web_lab1/jobs.html')


def privacy(request):
    return render(request, 'hospital/web_lab1/privacy.html')


@user_passes_test(lambda u: u.is_superuser)
def add_services_to_order(request):
    logger.info('admin adds services to order')
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


def statistics(request):
    logger.info('statistics loading start')
    visits = Visit.objects.all()
    total_sales = sum(visit.service.price for visit in visits)

    clients = Client.objects.all()
    today = date.today()
    total_clients = clients.count()
    total_age = sum(today.year - client.birthday.year for client in clients)
    average_age = 0
    if total_clients > 0:
        average_age = round(total_age / total_clients)

    full_dates = [item.date() for item in daterange(datetime.now())]
    dates_days = [int(dt.strftime("%d")) for dt in full_dates]

    monthly_visits = Visit.objects.filter(visit_date__year=full_dates[0].strftime('%Y'),
                                          visit_date__month=full_dates[0].strftime('%m'))
    logger.info('statistics loading end')
    plot_monthly_visits(monthly_visits, dates_days, full_dates)
    return render(request, 'hospital/statistics.html', {'total_sales': total_sales, 'average_age': average_age})


def daterange(cur_date):
    delta = timedelta(days=1)
    while True:
        yield cur_date
        if cur_date.strftime("%d") == '01':
            break
        cur_date -= delta


def plot_monthly_visits(monthly_sales, dates_days, full_dates):
    logger.info('executing monthly visits plotting')

    sales_count = [0 for i in range(len(full_dates))]

    for index, dt in enumerate(full_dates):
        for sale in monthly_sales:

            if dt == sale.visit_date.date():
                sales_count[index] += 1
    plt.switch_backend('agg')
    plt.clf()
    plt.cla()
    plt.close()

    plt.bar(dates_days, sales_count)
    plt.yticks(sales_count)
    plt.xticks(dates_days)

    plt.xlabel('день')
    plt.ylabel('посещения')
    plt.title('Посещения в месяце')
    plt.savefig('hospital/static/hospital/images/monthly_sales.png')


def unknown_page(request, unknown):
    return render(request, 'hospital/unknown_page.html', {'unknown_url': unknown})


def js_tasks(request):
    return render(request, 'hospital/web_lab3/js_tasks.html')


def js_task9(request):
    return render(request, 'hospital/web_lab3/js_task9.html')


def js_task11(request):
    return render(request, 'hospital/web_lab3/js_task11.html')

def js_task3(request):
    return render(request, 'hospital/web_lab3/js_task3.html')

def js_task5(request):
    return render(request, 'hospital/web_lab3/js_task5.html')