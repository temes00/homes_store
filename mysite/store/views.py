from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *

def root(request):
    products_list = Products.objects.filter(visible = 1).order_by('prior')
    for product in products_list:
        product.images = Images.objects.filter(product_id=product.id)
        if product.sale:
        	product.sale_price = int( product.price - ( product.price / 100 * product.sale ) )
    paginator = Paginator(products_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    meta = {
    }
    return render(request, 'store/main.html', {
        'products' : page_obj,
    })

def products_item(request, slug):
    product = get_object_or_404(Products, slug=slug)
    product.images = Images.objects.filter(product_id=product.id)
    if product.sale:
    	product.sale_price = int( product.price - ( product.price / 100 * product.sale ) )
    return render(request, 'store/product_page.html', {
        'item' : product
    })

def order(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    product.images = Images.objects.filter(product_id=product.id)
    if product.sale:
    	product.sale_price = int( product.price - ( product.price / 100 * product.sale ) )
    return render(request, 'store/order.html', {
    	'item' : product
    })

def order_create(request):
	params = request.POST.dict()
	product = Products.objects.get(slug=params["product_slug"])
	if product.sale:
		product.price = int( product.price - ( product.price / 100 * product.sale ) )
	order = Orders(
		name=str(params["firstname"]),
		lastname=str(params["lastname"]),
		email=str(params["email"]),
		phone=str(params["phoneNumber"]),
		comment=str(params["comment"]),
		product_id=product.id,
		price=product.price)
	order.save()
	message = (
    	'С вами свяжутся в ближайшее время для осуществеления сделки. Ваш заказ:\n'
		'Название дома: ' + str(product.name) + ' Сумма: ' + str( product.price ) + " Руб.\n"
		"Адрес: " + str(product.city) + " " + str(product.addres))
	mail_status = "Ok"
	try:
		send_mail(
		    'Спасибо за заказ на сайте "XYZ"',
		    message,
		    'prisonere@mail.ru',
		    [str(params["email"])],
		    fail_silently=False,
		)
	except Exception as e:
		mail_status = str(e)
	email = Mails(
		email=str(params["email"]), 
		body=str(message),
		status=mail_status)
	email.save()
	if mail_status == 'Ok':
		data = { 'error' : 0, 'message' : "Заказ успешно создан" }
	else:
		data = { 'error' : 1, 'message' : "Заказ успешно создан, но сообщение не отправлено (Подробности в админке)" }
	return JsonResponse(data)