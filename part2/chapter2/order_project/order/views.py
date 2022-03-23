from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.parsers import JSONParser

from order.models import Shop, Menu, Order, OrderFoodlist
from order.serializers import ShopSerializer, MenuSerializer


@csrf_exempt
def shop(request):
    if request.method == 'GET':
        shops = Shop.objects.all()
        # serializer = ShopSerializer(shops, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'order/shop_list.html', {'shop_list': shops})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def menu(request, shop):
    if request.method == 'GET':
        menu = Menu.objects.filter(shop=shop)
        # serializer = MenuSerializer(menu, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'order/menu_list.html', {'menu_list': menu, 'shop': shop})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def order(request):
    if request.method == 'GET':
        order_list = Order.objects.all()
        return render(request, 'order/order_list.html', {'order_list': order_list})

    elif request.method == 'POST':
        address = request.POST.get('address')
        shop = request.POST.get('shop')
        food_list = request.POST.getlist('menu')
        order_date = timezone.now()

        shop_item = Shop.objects.get(pk=int(shop))
        # Order에 Shop이 FK로 걸려있으므로 해당 shop 객체에서 '{FK 클래스(소문자)}_set' 사용
        shop_item.order_set.create(
            address=address,
            order_date=order_date,
            shop=int(shop)
        )

        # 주문 생성된 가장 마지막 id값으로 order 정보 가져오기
        order_item = Order.objects.get(pk=int(shop_item.order_set.latest('id').id))
        for food in food_list:
            order_item.orderfoodlist_set.create(food_name=food)

        return render(request, 'order/success.html')
