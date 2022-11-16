import weasyprint
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from io import BytesIO


def send_email_client(order):
    subject = 'My-shop - Заказ: {}'.format(order.id)
    message = 'Информация по вашему заказу.'
    email = EmailMessage(subject,
                         message,
                         'ilushamdmaa@yandex.ru',
                         [order.email])
    # Формирование PDF.
    html = render_to_string('pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS('static/css/css_pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # Прикрепляем PDF к электронному сообщению.
    email.attach('My-shop заказ номер:{}.pdf'.format(order.id),
                 out.getvalue(),
                 'application/pdf')
    # Отправка сообщения.
    res = email.send()
    return res