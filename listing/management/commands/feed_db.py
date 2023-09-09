import os
import random
from datetime import datetime

from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from listing.models import *

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        # Your code to populate the database goes here
        # Populate Currency model
        currency1 = Currency.objects.create(code='INR', name='Indian Rupee', symbol  ='₹')
        currency3 = Currency.objects.create(code='USD', name='United States Dollar', symbol='$')
        currency2 = Currency.objects.create(code='EUR', name='Euro', symbol='€')
        Currency.objects.create(code='JPY', symbol='¥', name='Japanese Yen')
        Currency.objects.create(code='GBP', symbol='£', name='Great British Pound')
        Currency.objects.create(code='AUD', symbol='$', name='Australian Dollar')
        Currency.objects.create(code='CAD', symbol='C$', name='Canadian Dollar')
        Currency.objects.create(code='CHF', symbol='Fr.', name='Swiss Franc')
        Currency.objects.create(code='CNY', symbol='¥', name='Chinese Yuan Renminbi')
        Currency.objects.create(code='HKD', symbol='$', name='Hong Kong Dollar')
        Currency.objects.create(code='NZD', symbol='$', name='New Zealand Dollar')
        Currency.objects.create(code='SEK', symbol='kr', name='Swedish Krona ')
        Currency.objects.create(code='NOK', symbol='kr', name='Norwegian Krone ')
        Currency.objects.create(code='DKK', symbol='kr', name='Danish Krone ')
        Currency.objects.create(code='SGD', symbol='$', name='Singapore Dollar')
        Currency.objects.create(code='MXN', symbol='$', name='Mexican Peso')
        Currency.objects.create(code='KRW', symbol='₩', name='South Korean Won')

        # Populate Product model
        # product1 = Product.objects.create(name='Product 1', description='This is product 1', is_purchaseable=True, maximum_qty=10, minimum_qty=1,height=0, weight=3.9)
        # product2 = Product.objects.create(name='Product 2', description='This is product 2', is_purchaseable=False, maximum_qty=20, minimum_qty=2,height=0, weight=3.9)
        # product3 = Product.objects.create(name='Product 3', description='This is product 3', is_purchaseable=True, maximum_qty=20, minimum_qty=2,height=0, weight=3.9)

        # # Populate Service model
        # service1 = Service.objects.create(name='Service 1', description='This is service 1', is_purchaseable=True, maximum_qty=10, minimum_qty=1,available_at=datetime(2023, 9, 15, 9, 0, 0,0,None), not_available_at=datetime(2023, 9, 15, 9, 0, 0,0,None))
        # service2 = Service.objects.create(name='Service 2', description='This is service 2', is_purchaseable=False, maximum_qty=20, minimum_qty=2,available_at=datetime(2023, 9, 15, 9, 0, 0,0,None), not_available_at=datetime(2023, 9, 15, 9, 0, 0,0,None))
        # service3 = Service.objects.create(name='Service 3', description='This is service 3', is_purchaseable=False, maximum_qty=20, minimum_qty=2,available_at=datetime(2023, 9, 15, 9, 0, 0,0,None), not_available_at=datetime(2023, 9, 15, 9, 0, 0,0,None))



        # Create a property listing
        product1 = Product.objects.create(
            name='Property Listing',
            description='A beautiful 3-bedroom house in the city center.',
            height=10,
            weight=1000
        )

        # Create a land listing
        product2 = Product.objects.create(
            name='Land Listing',
            description='A 10-acre plot of land in the countryside.',
            height=0,
            weight=10000
        )

        # Create a haircut service
        service1 = Service.objects.create(
            name='Haircut',
            description='A professional haircut at our salon.',
            available_at='2023-09-10 09:00:00',
            not_available_at='2023-09-10 18:00:00'
        )

        # Create an Ecommerce product
        product3 = Product.objects.create(
            name='Ecommerce Product',
            description='A high-quality product available for purchase online.',
            height=5,
            weight=1
        )

        # Create a billboard booking service
        service2 = Service.objects.create(
            name='Billboard Booking',
            description='Book a billboard to advertise your business.',
            available_at='2023-09-10 09:00:00',
            not_available_at='2023-09-10 18:00:00'
        )

        # Create a renting listing
        product4 = Product.objects.create(
            name='Renting Listing',
            description='A spacious apartment available for rent.',
            height=3,
            weight=500
        )

        # Create a tradesman work listing
        service3 = Service.objects.create(
            name='Tradesman Work Listing',
            description='Hire a skilled tradesman for your home improvement project.',
            available_at='2023-09-10 09:00:00',
            not_available_at='2023-09-10 18:00:00'
        )

        # Create a second-hand product
        product5 = Product.objects.create(
            name='Second-hand Product',
            description='A gently used item in good condition.',
            height=2,
            weight=0.5
        )



        # Populate Units model
        # Quantity units
        unit1 = Unit.objects.create(name='Unit', symbol='unit', unit_type='Quantity', conversion_factor=1)
        Unit.objects.create(name='Dozen', symbol='doz', unit_type='Quantity', conversion_factor=12)
        Unit.objects.create(name='Hundred', symbol='hundred', unit_type='Quantity', conversion_factor=100)
        Unit.objects.create(name='Thousand', symbol='thousand', unit_type='Quantity', conversion_factor=1000)

        # Time units
        unit2 = Unit.objects.create(name='Second', symbol='s', unit_type='Time', conversion_factor=1)
        Unit.objects.create(name='Minute', symbol='min', unit_type='Time', conversion_factor=60)
        Unit.objects.create(name='Hour', symbol='h', unit_type='Time', conversion_factor=3600)
        Unit.objects.create(name='Day', symbol='day', unit_type='Time', conversion_factor=86400)
        Unit.objects.create(name='Week', symbol='week', unit_type='Time', conversion_factor=604800)

        # Area units
        unit3 = Unit.objects.create(name='Square meter', symbol='m²', unit_type='Area', conversion_factor=1)
        Unit.objects.create(name='Square centimeter', symbol='cm²', unit_type='Area', conversion_factor=0.0001)
        Unit.objects.create(name='Square millimeter', symbol='mm²', unit_type='Area', conversion_factor=0.000001)
        Unit.objects.create(name='Acre', symbol='acre', unit_type='Area', conversion_factor=4046.86)
        Unit.objects.create(name='Cent', symbol='cent', unit_type='Area', conversion_factor=40.4686)
        Unit.objects.create(name = 'Square foot' ,symbol = 'ft²' ,unit_type = 'Area' ,conversion_factor = 0.092903)

        # Weight units
        unit4 = Unit.objects.create(name = 'Kilogram' ,symbol = 'kg' ,unit_type = 'Weight' ,conversion_factor = 1)
        Unit.objects.create(name = 'Gram' ,symbol = 'g' ,unit_type = 'Weight' ,conversion_factor = 0.001)

        # Length units
        unit5 = Unit.objects.create(name = 'Meter' ,symbol = 'm' ,unit_type = 'Length' ,conversion_factor = 1)
        unit6 = Unit.objects.create(name = 'Centimeter' ,symbol = 'cm' ,unit_type = 'Length' ,conversion_factor = 0.01)

        self.stdout.write('All Units are created')

        # Populate Price model
        price1 = Price.objects.create(mrp=100.0, saleprice=80.0, offerprice=70.0, currency=currency1, listing=product2, unit=unit1)
        price2 = Price.objects.create(mrp=200.0, saleprice=180.0, offerprice=150.0, currency=currency2, listing=product3, unit=unit2)
        price3 = Price.objects.create(mrp=250.0, saleprice=210.0, offerprice=150.0, currency=currency3, listing=product1, unit=unit3)
        price4 = Price.objects.create(mrp=250.0, saleprice=210.0, offerprice=150.0, currency=currency1, listing=service2, unit=unit4)
        price5 = Price.objects.create(mrp=200.0, saleprice=180.0, offerprice=150.0, currency=currency1, listing=service3, unit=unit5)
        price6 = Price.objects.create(mrp=250.0, saleprice=210.0, offerprice=150.0, currency=currency1, listing=service1, unit=unit6)
        price6 = Price.objects.create(mrp=250.0, saleprice=210.0, offerprice=150.0, currency=currency1, listing=product4, unit=unit6)
        price6 = Price.objects.create(mrp=250.0, saleprice=210.0, offerprice=150.0, currency=currency1, listing=product5, unit=unit6)

        # Populate Media model
        media_dir = 'media/'
        for filename in os.listdir(media_dir):
            if filename.endswith('.jpeg'):
                media_type = 'Image'
            elif filename.endswith('.mp4'):
                media_type = 'Video'
            else:
                continue

            with open(os.path.join(media_dir, filename), 'rb') as f:
                file = File(f)
                Media.objects.create(media_type=media_type, file=file,listing=random.choice([
                    product1,product2,product3,product4,product5,service1,service2,service3
                ]))

        self.stdout.write('Dummy Data added to Database')
