import datetime
from datetime import date
from time import strptime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render, reverse, redirect
from .forms import ClientSignUpForm, PassportForm
from service.models import Service, ServiceCategory
from doctor.models import Doctor
from order.models import Order, OrderService

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
    services = Service.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'client/info.html', context)


def order(request):
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


def finish_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            client = request.user.client
            services = request.POST.getlist('service_id')
            dates = request.POST.getlist('data[]')
            doctors = request.POST.getlist('doctor')
            print(client, services, dates, doctors)
            print(strptime(dates[0], '%Y-%m-%d'))

            # order = Order.objects.create(client=client, date=datetime.date.today())
            # for service_id, date, doctor_id in zip(services, dates, doctors):
            #     service = Service.objects.get(pk=service_id)
            #     doctor = Doctor.objects.get(pk=doctor_id)
            #
            #     OrderService.objects.create(order=order, service=service, doctor=doctor, date=date)

            return render(request, 'client/success_page.html')  # Replace 'success_page' with the actual URL or name of the success page

    else:
        return redirect('login')  # Replace 'login' with the actual URL or name of the login page