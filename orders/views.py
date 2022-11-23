import json
import os

from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from store import settings
from alert_admin_bot.send_message_bot import send_alert_bot

from .models import OrderItem, Order, DeliveryMethod, PaymentMethod
from .forms import OrderCreateForm, Oplata
from cart.cart import Cart
from django.shortcuts import render
from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import weasyprint
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from .send_email_for_order import send_email_client


# def proof_of_payment(request):
#     if request.method == 'POST':
#         user_p = request.user
#         data = json.load(request)
#         order_id = data.get('order_id')
#         order = Order.objects.get(id=int(order_id))
#         res = ''
#         if int(data.get('proof_pay_inp')) == order.get_total_cost():
#             order.paid = True
#             order.save()
#             res = 'Оплата прошла, спасибо за оплату'
#             send_email_client(order)
#         else:
#             res = 'Оплата не прошла'
#             print(res)
#     return HttpResponse(res)


def proof_of_payment_page(request,order_id):
    cart = Cart(request)
    order = Order.objects.get(id=order_id)
    sum_order = order.get_total_cost()
    form = Oplata()
    os = order.get_total_cost
    print(order.check_payment_method())
    print('*' * 10)
    if request.method == "POST":
        error = ''
        print('10')
        form = Oplata(request.POST)
        if form.is_valid():
            print(sum_order)
            sum_form = int(form.cleaned_data.get('paid_order_sum'))
            if sum_form == sum_order:
                order.paid = True
                order.save()
                send_email_client(order)
                cart.clear()
                order_id = int(order.id)
                print('Заказ оплачен')
                send_alert_bot( f' http://127.0.0.1:8000{order.get_absolute_url()}','Заказ')
                return redirect(f'http://127.0.0.1:8000/orders/created_order/{order_id}/')
            else:
                error = 'Сумма не верна'
                return render(request, 'paid_click.html',
                       {'order': order, 'sum_order': sum_order, 'form': form,'error':error})
    return render(request,'paid_click.html',
                          {'order': order,'sum_order': sum_order,'form':form})


def created_order(request,order_id):
    order = Order.objects.get(pk=order_id)
    code = order.code
    print('*****')
    print(code)
    return render(request, 'created.html',{order:'order',code:'code'})



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        print(request.POST)
        form = OrderCreateForm(request.POST)
        user_p = request.user
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            order_id = int(order.id)
            if not order.check_payment_method():
                print(order.check_payment_method)
                send_email_client(order)
                cart.clear()
                send_alert_bot( f' http://127.0.0.1:8000 {order.get_absolute_url()}','Заказ')
                return redirect('created_order',order_id=order_id)
            return redirect('proof_of_payment_page',order_id=order_id)
    else:
        # frm = OrderCreateForm()
        # initial_data = {
        #     'delivery_method': frm.fields['delivery_method'][1]
        # }
        # form.fields['delivery_method'].initial = form.fields['delivery_method'][0]
        default_delivery = DeliveryMethod.objects.get(id=1)
        default_paid = PaymentMethod.objects.get(id=1)

        form = OrderCreateForm(initial={'delivery_method': default_delivery,'payment_method':default_paid})
    return render(request, 'create.html',
                  {'cart': cart, 'form': form})



