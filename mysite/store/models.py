from django.db import models
from tinymce.models import HTMLField

class Products(models.Model):
    name = models.CharField(max_length=255,default="")
    slug = models.CharField(max_length=255,default="")
    visible = models.BooleanField(default=False)
    prior = models.IntegerField(default=0)
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_description = models.CharField(max_length=255, blank=True, null=True)
    seo_keywords = models.CharField(max_length=255, blank=True, null=True)
    h1 = models.CharField(max_length=255, blank=True, null=True)
    description = HTMLField()
    price = models.IntegerField()
    sale = models.IntegerField(default=0)
    city = models.CharField(max_length=255,default="")
    addres = models.CharField(max_length=255,default="")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Товары'
        verbose_name_plural='Товары'

    def __str__(self):
        return self.name

class Images(models.Model):
        name = models.CharField(max_length=100)
        product_id = models.ForeignKey('Products', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Product_id')
        image = models.ImageField(upload_to='images/', blank=True)

        class Meta:
            verbose_name = 'Картинка'
            verbose_name_plural = 'Картинки'

        def __str__(self):
            return self.name

class Orders(models.Model):
    name = models.CharField(max_length=255,default="")
    lastname = models.CharField(max_length=255,default="")
    phone = models.CharField(max_length=255,default="")
    email = models.CharField(max_length=255,default="")
    comment = models.TextField(default="")
    product_id = models.IntegerField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Заказы'
        verbose_name_plural='Заказы'

    def __str__(self):
        return self.name

class Mails(models.Model):
    email = models.CharField(max_length=255)
    body = HTMLField()
    status =  models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Рассылка'
        verbose_name_plural='Рассылка'

    def __str__(self):
        return self.name