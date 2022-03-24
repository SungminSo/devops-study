from django.urls import path

from boss import views

urlpatterns = [
    path('orders/<int:shop>', views.order_list, name='order_list'),
    path('estimated-time/', views.estimated_time_input, name='estimated_time_input'),
    # path('menus/<int:shop>', views.menu, name='menu'),
    # path('orders/', views.order, name='order'),
]
