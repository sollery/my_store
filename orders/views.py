import os

from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from store import settings
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import render
from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


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
            met = order.delivery_method
            # очистка корзины
            cart.clear()
            # запуск асинхронной задачи

            print(order.id)
            os = order.get_total_cost
            # send_mail(
            #     subject='order',
            #     message='Уважаемая {} {} мы приняли ваш заказ в обработку, сумма вашего заказа: {}, cпособ доставки {} '
            #             'Спасибо за заказ! будем ждать вас снова'.format(form.cleaned_data['first_name'],
            #                                                              form.cleaned_data['last_name'],
            #                                                              os, met),
            #     from_email='ilushamdmaa@yandex.ru',
            #     recipient_list=['itivih70@yandex.ru'],
            # )
            subject = 'Z-shop - Заказ: {}'.format(order.id)
            message = 'Информация по вашему заказу.'
            email = EmailMessage(subject,
                                 message,
                                 'ilushamdmaa@yandex.ru',
                                 [order.email])
            # Формирование PDF.
            html = render_to_string('pdf.html', {'order': order})
            out = BytesIO()
            stylesheets=[weasyprint.CSS('static/css/css_pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)
            # Прикрепляем PDF к электронному сообщению.
            email.attach('z-shop заказ номер:{}.pdf'.format(order.id),
                         out.getvalue(),
                         'application/pdf')
            # Отправка сообщения.
            email.send()
            return render(request, 'created.html',
                          {'order': order,'user_p': user_p,'o': os})
    else:
        form = OrderCreateForm
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
