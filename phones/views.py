from django.shortcuts import render
from django.conf import settings
import csv
from phones.models import Phone
import operator
from datetime import datetime, date, time


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    phone_list = []
    for i in range(len(phones)):
        phone_list.append({
            'id': phones[i].id,
            'name': phones[i].name,
            'image': phones[i].image,
            'price': phones[i].price,
            'release_date': phones[i].release_date,
            'lte_exists': phones[i].lte_exists,
            'slug': phones[i].slug
        })
    if request.GET.get('sort'):
        sort = request.GET.get('sort')
        if sort=='name':
            phone_list = sorted(phone_list, key=lambda k: k['name'])
        if sort=='min_price':
            phone_list = sorted(phone_list, key=lambda k: k['price'])
        if sort=='max_price':
            phone_list = sorted(phone_list, key=lambda k: k['price'], reverse=True)
    context = {
        'phones': phone_list
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_info = Phone.objects.get(slug=slug)
    if phone_info.lte_exists:
        lte_exists = 'есть'
    else:
        lte_exists = 'нет'
    release_date = phone_info.release_date.strftime('%d.%m.%Y') + 'г.'
    context = {
        'name': phone_info.name,
        'image': phone_info.image,
        'price': phone_info.price,
        'release_date': release_date,
        'lte_exists': lte_exists
    }
    return render(request, template, context)
