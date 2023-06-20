import datetime
import logging
from datetime import date
from time import strptime

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from .forms import ClientSignUpForm, PassportForm
from service.models import Service, ServiceCategory
from doctor.models import Doctor
from order.models import Order, OrderService

User = get_user_model()
logger = logging.getLogger('main')


def register_client(request):
    logger.info('client register')
    form = ClientSignUpForm(request.POST or None)
    passport_form = PassportForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid() and passport_form.is_valid():
            try:
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
            except IntegrityError:
                return HttpResponse('<h1>Пользователь с таким номером паспорта уже существует!</h1>')
        else:
            print(form.errors)
    data = {
        'form': form,
        'passport_form': passport_form
    }
    return render(request, 'client/signup_client.html', data)


def is_not_superuser(user):
    return not user.is_superuser


@user_passes_test(is_not_superuser)
@permission_required('client.view_client', raise_exception=True)
def info(request):
    logger.info('client page')
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'client/info.html', context)


@user_passes_test(is_not_superuser)
@permission_required('client.view_client', raise_exception=True)
def order(request):
    logger.info('client order')
    if request.method == 'POST':

        selected_services = request.POST.getlist('checkbox')
        if selected_services:
            services = Service.objects.filter(id__in=selected_services)
            doctors = Doctor.objects.all()

            total_cost = 0.0
            for service in services:
                total_cost += service.price

            return render(request, 'client/order.html',
                          {'services': services, 'doctors': doctors, 'date': str(date.today()),
                           'cost': round(total_cost, 2)})

    return redirect('/info/')


@user_passes_test(is_not_superuser)
@permission_required('client.view_client', raise_exception=True)
def finish_order(request):
    logger.info('client submitting order')
    if request.user.is_authenticated:
        if request.method == 'POST':
            client = request.user.client
            services = request.POST.getlist('service_id')
            dates = request.POST.getlist('data[]')
            doctors = request.POST.getlist('doctor')

            order = Order.objects.create(client=client, date=datetime.date.today())
            for service_id, date, doctor_id in zip(services, dates, doctors):
                service = Service.objects.get(pk=service_id)
                doctor = Doctor.objects.get(pk=doctor_id)
                OrderService.objects.create(order=order, service=service, doctor=doctor, date=date)

            return render(request, 'client/success_page.html')

    else:
        return redirect('login')
