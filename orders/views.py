import json
import os

from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from store import settings
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
                # print(sum_order)
                order.paid = True
                order.save()
                send_email_client(order)
                cart.clear()
                return render(request, 'created.html',
                              {'order': order, 'o': os})
            else:
                error = 'Сумма не верна'
                return render(request, 'paid_click.html',
                       {'order': order, 'sum_order': sum_order, 'form': form,'error':error})
    return render(request,'paid_click.html',
                          {'order': order,'sum_order': sum_order,'form':form})

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
            # if met == 'Курьером'
            # очистка корзины
            os = order.get_total_cost
            # запуск асинхронной задачи
            if not order.check_payment_method():
                print(order.check_payment_method)
                send_email_client(order)
                cart.clear()
            return render(request, 'created.html',
                          {'order': order,'user_p': user_p,'o': os})
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
# Create your views here.


# def fetch_pdf_resources(uri, rel):
#     if uri.find(settings.MEDIA_URL) != -1:
#         path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
#     elif uri.find(settings.STATIC_URL) != -1:
#         path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
#     else:
#         path = None
#     return path
#
#
# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result,
#                             encoding='utf-8',
#                             link_callback=fetch_pdf_resources)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
#
#
# data = {
#     "company": "Dennnis Ivanov Company",
#     "address": "123 Street name",
#     "city": "Vancouver",
#     "state": "WA",
#     "zipcode": "98663",
#
#     "phone": "555-555-2345",
#     "email": "youremail@dennisivy.com",
#     "website": "dennisivy.com",
# }
#
#
# # Opens up page as PDF
# class ViewPDF(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('pdf.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')
#
#
# # Automaticly downloads to PDF file
# class DownloadPDF(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('pdf.html', data)
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "Invoice_%s.pdf" % ("12341231")
#         content = "attachment; filename='%s'" % (filename)
#         response['Content-Disposition'] = content
#         return response


@staff_member_required
def admin_order_pdf(request, order_id):
     order = get_object_or_404(Order, id=order_id)
     html = render_to_string('pdf.html', {'order': order})
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = 'filename=\
     "order_{}.pdf"'.format(order.id)
     weasyprint.HTML(string=html).write_pdf(response)
     return response
