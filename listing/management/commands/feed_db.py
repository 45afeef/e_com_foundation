from django.core.management.base import BaseCommand

import pandas as pd

from listing.models import Price, Listing, Product, Service, Currency, Unit, Media

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        # Load the data from the Excel file
        xls = pd.ExcelFile('data.xlsx')

        # Load the sheets into dataframes
        units_df = xls.parse('units')
        currencies_df = xls.parse('currencies')
        products_df = xls.parse('products')
        services_df = xls.parse('services')

        # Populate the Units
        for index, row in units_df.iterrows():
            Unit.objects.create(name=row['name'], symbol=row['symbol'], unit_type=row['unit_type'], conversion_factor=row['conversion_factor'])

        # Populate the Currencies
        for index, row in currencies_df.iterrows():
            Currency.objects.create(code=row['code'], name=row['name'], symbol=row['symbol'])

        # Helper function to create a Listing, Price and Media
        def create_listing_price_and_media(df_row, listing_type):
            # Create the listing
            listing = listing_type(name=df_row['name'], description=df_row['description'], min_qty=df_row['minqty'], max_qty=df_row['maxqty'])
            listing.save()

            # Get the currency and unit objects
            currency = Currency.objects.get(name='Indian Rupee')  # Replace 'Your Currency Name' with your actual currency name
            print(df_row['unit'])
            unit = Unit.objects.get(name=df_row['unit'])

            # Create the price
            Price.objects.create(
                mrp=df_row['mrp'] if pd.notnull(df_row['mrp']) else None,
                saleprice=df_row['sale_price'],
                offerprice=df_row['offer_price'] if pd.notnull(df_row['offer_price']) else None,
                currency=currency, 
                listing=listing, 
                unit=unit
            )

            # Create the media
            for i in range(1, 5):
                media_file_name = df_row['image'] + str(i) + '.jpeg'
                Media.objects.create(media_type='Image', file='media/' + media_file_name, listing=listing)

        # Populate the Products, Prices and Media
        for index, row in products_df.iterrows():
            create_listing_price_and_media(row, Product)

        # Populate the Services, Prices and Media
        for index, row in services_df.iterrows():
            create_listing_price_and_media(row, Service)
