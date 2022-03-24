from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.parsers import JSONParser

from order.models import Order


@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        order_list = Order.objects.all()
        return render(request, 'delivery/order_list.html', {'order_list': order_list})
    if request.method == 'POST':
        order_item = Order.objects.get(pk=int(request.POST.get('order_id')))
        order_item.deliver_finish = True
        order_item.save()
        return render(request, 'delivery/success.html')