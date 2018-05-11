from django.conf.urls import url

from main.views import *

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^products/$', products_view, name='product_view'),
    url(r'^shop/$', shop_view, name='shop_view'),
    url(r'^add_to_cart/$', add, name='add_to_cart'),
    url(r'^delete/$', delete_cart_item, name='delete_from_cart'),
    url(r'^cart/$', cart_view, name='cart_view'),
    url(r'^send_message', send_message_with_cart, name='send_message'),
]

