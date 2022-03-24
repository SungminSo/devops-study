from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.parsers import JSONParser

from order.models import Order


@csrf_exempt
def order_list(request, shop):
    if request.method == 'GET':
        order_list = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', {'order_list': order_list})


@csrf_exempt
def estimated_time_input(request):
    if request.method == 'POST':
        order_item = Order.objects.get(pk=int(request.POST.get('order_id')))
        order_item.estimated_time = int(request.POST.get('estimated_time'))
        order_item.save()
        return render(request, 'boss/success.html', {'shop': int(order_item.shop.id)})
    else:
        return HttpResponse(status=405)