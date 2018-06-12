# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import smart_unicode


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/product_images', verbose_name='Image')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    is_offer = models.BooleanField(default=False, verbose_name='Специальное предложение',
                                   help_text='Поставьте галочку если на текущий товар действует спецаильное предложение')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Slider(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    slogan = models.CharField(max_length=500, verbose_name='Слоган', help_text='Не более 100 символов')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/slider', verbose_name='Картинка', help_text='Размер 432x275')
    price = models.CharField(max_length=255, verbose_name='Цена (если это товар)', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)
