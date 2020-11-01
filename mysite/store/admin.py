from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.template.defaulttags import register
from django.shortcuts import render
from django.db.models import Count
from django import forms

from .models import *

class ImagesInline(admin.TabularInline):
    model = Images

class ProductsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'slug', 'prior', 'visible', 'price', 'sale', 'city', 'addres', 'created')
	inlines = [
        ImagesInline
    ]

class OrdersAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'lastname', 'phone', 'email', 'product_id', 'price', 'created')

class MailsAdmin(admin.ModelAdmin):
	list_display = ('id', 'email', 'body', 'status', 'created')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Mails, MailsAdmin)
