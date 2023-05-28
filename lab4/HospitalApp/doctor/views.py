import datetime

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import Group
from django.views.decorators.http import require_POST
from .forms import DoctorSignUpForm
from order.models import OrderService, Order
from visit.models import Visit

User = get_user_model()


def register_doctor(request):
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


def info(request):
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
    return render(request, 'doctor/info.html',
                  {'order_services': order_services,
                   'date': str(datetime.date.today()), 'total_cost': total_cost})


@require_POST
def complete_service(request, item_id):
    order_service = OrderService.objects.get(pk=item_id)

    visit = Visit.objects.create(
        doctor=order_service.doctor,
        client=order_service.order.client,
        visit_date=order_service.date,
        service=order_service.service
    )

    visit.save()
    if not len(OrderService.objects.filter(order=order_service.order)):
        Order.objects.get(order_service.order.id)
    order_service.delete()
    return redirect('/doctor/info')
