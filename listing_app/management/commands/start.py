from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Runs makemigrations, migrate, creates a superuser and populate databases'

    def handle(self, *args, **options):
        # Run makemigrations
        self.stdout.write('Running makemigrations...')
        call_command('makemigrations')

        # Run migrate
        self.stdout.write('Running migrate...')
        call_command('migrate')

        # Create superuser
        self.stdout.write('Creating superuser...')
        User.objects.create_superuser('admin', 'admin@example.com', '123')

        # Populate the database
        self.stdout.write('Populating Database')
        call_command('feed_db')

        self.stdout.write('Done.')

