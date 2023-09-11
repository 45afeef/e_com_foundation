from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Clear the database'

    def handle(self, *args, **options):
        # Get all models in the 'listing' app
        models = apps.get_app_config('listing_app').get_models()

        # Iterate over all models and delete all objects
        for model in models:
            model.objects.all().delete()

        self.stdout.write('Database cleared')
