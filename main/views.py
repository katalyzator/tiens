# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from carton.cart import Cart
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from django.template import Template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt

from main.models import Product
from tiens.settings import BASE_DIR


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.add(product, price=product.price)

    return render_to_response('partial/basket_values.html', dict(cart=cart))


def delete_cart_item(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.remove(product)

    return render_to_response('partial/basket_values.html', dict(cart=cart))


def index_view(request):
    products = Product.objects.filter(is_active=True)
    context = {"products": products}
    template = 'index.html'

    return render(request, template, context)


def products_view(request):
    context = {}
    template = 'products.html'

    return render(request, template, context)


def shop_view(request):
    context = {}
    template = 'shop.html'

    return render(request, template, context)


def cart_view(request):
    context = {}
    template = 'cart.html'

    return render(request, template, context)


@csrf_exempt
def send_message_with_cart(request):
    import os
    f = open(os.path.join(BASE_DIR, "templates/mail.html"))

    name = request.POST.get('name')
    phone = request.POST.get('phone_number')

    cart = Cart(request.session)

    content = f.read()
    f.close()
    context = Context(dict(name=name, phone=phone, cart=cart))
    template = Template(content)
    mail = EmailMessage('Заявка на покупку продукта', template.render(context), to=['odaniaro@gmail.com'])
    mail.content_subtype = 'html'
    mail.send()

    return JsonResponse(dict(result="ok"))
