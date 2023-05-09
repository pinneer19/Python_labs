
from django.shortcuts import render
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

    return render(request, 'service/info.html', context)
