# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from carton.cart import Cart
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from main.models import Product


def add(request):

    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.add(product, price=product.price)

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
