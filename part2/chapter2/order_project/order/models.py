from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)


class Menu(models.Model):
    # on_delete = models.CASCADE: Shop 테이블에서 레코드가 삭제될 시 해당 외래키를 가진 Menu 레코드도 모두 삭제됨
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)


class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    address = models.CharField(max_length=40)
    estimated_time = models.IntegerField(default=-1, help_text='예상소요시간')
    deliver_finish = models.BooleanField(default=False)


class OrderFoodlist(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
