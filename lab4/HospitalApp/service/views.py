from django.shortcuts import render, redirect
from .models import Service, ServiceCategory


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
    print(dir(user))
    print(user.groups)
    if user.is_superuser:
        # TODO
        return render(request, 'service/info.html', context)
    elif user.groups.filter(name='Doctor').exists():
        return redirect('doctor/info.html', context)
    elif user.groups.filter(name='Client').exists():
        return redirect('client/info.html', context)
    else:
        return redirect('error')
