from django.contrib import admin

from .models import (
    Image,
    Product,
    Order,
    Mail
)


class ImagesInline(admin.TabularInline):
    model = Image


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'slug', 'prior', 'visible',
        'price', 'sale', 'city', 'addres', 'created'
    )
    inlines = [
        ImagesInline
    ]


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'lastname', 'phone',
        'email', 'product_id', 'price', 'created'
    )


class MailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'body', 'status', 'created')


admin.site.register(Product, ProductsAdmin)
admin.site.register(Order, OrdersAdmin)
admin.site.register(Mail, MailsAdmin)
