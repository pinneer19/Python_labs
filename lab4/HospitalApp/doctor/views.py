import datetime
import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import Group
from django.views.decorators.http import require_POST
from .forms import DoctorSignUpForm
from order.models import OrderService, Order
from visit.models import Visit
from visit.forms import VisitForm

User = get_user_model()
logger = logging.getLogger('main')


def register_doctor(request):
    logger.info('doctor register')
    form = DoctorSignUpForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            client = form.save(commit=False)
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )

            group = Group.objects.get(name='doctor')
            group.user_set.add(user)
            client.user = user

            user.save()

            return redirect('/login/')
        else:
            print(form.errors)

    data = {
        'form': form
    }
    return render(request, 'doctor/signup_doctor.html', data)


def is_not_superuser(user):
    return not user.is_superuser


@user_passes_test(is_not_superuser)
@permission_required('doctor.view_doctor', raise_exception=True)
def info(request):
    logger.info('doctor page')
    selected_date = request.POST.get('date')

    doctor = request.user.doctor
    if selected_date:
        order_services = OrderService.objects.filter(doctor=doctor, date=selected_date)
    else:
        order_services = OrderService.objects.filter(doctor=doctor)

    total_cost = 0.0
    for order_service in order_services:
        total_cost += order_service.service.price

    if total_cost == 0.0:
        total_cost = 'Нет заказанных услуг'
    else:
        total_cost = f'Итоговая стоимость заказанных услуг: {total_cost} byn'
    return render(request, 'doctor/info.html',
                  {'order_services': order_services,
                   'date': str(datetime.date.today()), 'total_cost': total_cost})


@user_passes_test(is_not_superuser)
@permission_required('doctor.view_doctor', raise_exception=True)
def complete_service(request, item_id):
    logger.info('doctor complete ordered service')
    order_service = OrderService.objects.get(pk=item_id)
    form = VisitForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            visit = Visit.objects.create(
                doctor=order_service.doctor,
                client=order_service.order.client,
                visit_date=order_service.date,
                service=order_service.service,
                diagnosis=form.cleaned_data['diagnosis']
            )

            if len(OrderService.objects.filter(order=order_service.order)) == 1:
                Order.objects.get(id=order_service.order.id).delete()
            else:
                order_service.delete()
            return redirect('/doctor/info/')

        else:
            print(form.errors)

    data = {
        'form': form
    }

    return render(request, 'doctor/complete_service.html', {'form': form})
