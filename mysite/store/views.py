from django.conf import settings

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Product, Order, Mail

from .utils import get_sale_price

from .forms import OrderCreateForm

HEAD_OF_MAIL = 'Спасибо за заказ на сайте "XYZ"'
ORDER_SUCCESS_MESSAGE = 'Заказ успешно создан'
ORDER_FAIL_MESSAGE = \
    'Заказ успешно создан, но сообщение не отправлено (Подробности в админке)'


def root(request):
    products_list = Product.objects.filter(visible=1).order_by('prior')
    paginator = Paginator(products_list, 3)

    page_number = request.GET.get('page') or 1
    page_obj = paginator.page(page_number)
    for product in page_obj.object_list:
        if product.sale:
            product.sale_price = get_sale_price(
                price=product.price,
                sale=product.sale
            )
    return render(request, 'store/main.html', {
        'products': page_obj,
    })


def products_item(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if product.sale:
        product.sale_price = get_sale_price(
                price=product.price,
                sale=product.sale
            )
    return render(request, 'store/product_page.html', {
        'item': product
    })


def order(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if product.sale:
        product.sale_price = get_sale_price(
                price=product.price,
                sale=product.sale
            )
    return render(request, 'store/order.html', {
        'item': product
    })


def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            params = request.POST.dict()
            product = Product.objects.get(slug=params["product_slug"])
            if product.sale:
                product.price = get_sale_price(
                        price=product.price,
                        sale=product.sale
                    )
            Order.objects.create(
                name=str(params["name"]),
                lastname=str(params["lastname"]),
                email=str(params["email"]),
                phone=str(params["phone"]),
                comment=str(params["comment"]),
                product_id=product.id,
                price=product.price,
            )
            product_data = {
                'name': str(params["name"]),
                'price': str(product.price),
                'city': str(product.city),
                'addres': str(product.addres),
            }
            message = render_to_string(
                "store/mails/success.html",
                product_data,
            )
            mail_status = "Ok"
            try:
                send_mail(
                    HEAD_OF_MAIL,
                    message,
                    settings.DEFAULT_COMPANY_EMAIL,
                    [str(params["email"])],
                    fail_silently=False,
                )
            except Exception as e:
                mail_status = str(e)
            email = Mail(
                email=str(params["email"]),
                body=str(message),
                status=mail_status,
            )
            email.save()
            if mail_status == 'Ok':
                data = {'error': 0, 'message': ORDER_SUCCESS_MESSAGE}
            else:
                data = {'error': 1, 'message': ORDER_FAIL_MESSAGE}
            print('ready!')
            return JsonResponse(data)
        else:
            data = {}
            data['error'] = 1
            data['message'] = ''
            for field in form.errors:
                data['message'] = \
                    (data['message'] + " " + form.errors[field].as_text())
            return JsonResponse(data)
    return JsonResponse('Not found', status=404)
