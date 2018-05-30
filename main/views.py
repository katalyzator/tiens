# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from carton.cart import Cart
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from django.template import Template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt

from main.models import Product, Slider
from tiens.settings import BASE_DIR


@csrf_exempt
def add(request, id):
    cart = Cart(request.session)
    product = Product.objects.get(id=id)
    cart.add(product, price=product.price)

    return render_to_response('partial/basket_values.html', dict(cart=cart))


@csrf_exempt
def delete_cart_item(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.remove(product)

    return render_to_response('partial/basket_values.html', dict(cart=cart))


@csrf_exempt
def ajax_product_detail(request, id):
    product = Product.objects.get(id=id)

    return render_to_response('partial/_product_detail.html', dict(product=product))


def index_view(request):
    products = Product.objects.filter(is_active=True)
    sliders = Slider.objects.all()

    context = {"products": products, "sliders": sliders}
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
