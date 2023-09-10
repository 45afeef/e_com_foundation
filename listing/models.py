from django.db import models
from django.utils.html import format_html

class Price(models.Model):
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    saleprice = models.DecimalField(max_digits=10, decimal_places=2)
    offerprice = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)

    def __str__(self):
        return f'Price: {self.saleprice} {self.currency.code} per {self.unit.symbol}'

class Media(models.Model):
    MEDIA_TYPES = (
        ('Image', 'Image'),
        ('Video', 'Video'),
    )
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='media/')
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Media: {self.media_type}'
    
    def preview(self):
        if self.media_type == 'Video':
            return format_html('<video width="150" controls><source src="{}" type="video/mp4"></video>', self.file.url)
        elif self.media_type == 'Image':
            return format_html('<img src="{}" width="150" />', self.file.url)
        else:
            return 'Media type not supported in preview'
    preview.short_description = 'Preview Of Media'



class Listing(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        abstract = False
    
    def __str__(self):
        return self.name


class Product(Listing):
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Service(Listing):
    available_at = models.DateTimeField()
    not_available_at = models.DateTimeField()
    
    def __str__(self):
        return self.name


class Currency(models.Model):
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=3)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Unit(models.Model):
    UNIT_TYPES = (
        ('Quantity', 'Quantity'),
        ('Weight', 'Weight'),
        ('Volume', 'Volume'),
        ('Length', 'Length'),
        ('Time', 'Time'),
        ('Area', 'Area'),
    )
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=3)
    unit_type = models.CharField(max_length=8, choices=UNIT_TYPES)
    conversion_factor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
