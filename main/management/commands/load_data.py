from django.core.management.base import BaseCommand, CommandError
from main.models import City, Country

 
class Command(BaseCommand):
    help = "Closes the specified poll for voting"

 
    def handle(self, *args, **options):
        print('Start command!!!!')
        Country.objects.all().delete()
        City.objects.all().delete()
        countries = ['Ukraine', 'USA', 'UK']
        for country in countries:
            record = Country()
            record.alias = country
            record.name = country
            record.save()
            cities = ['Kherson', 'Odessa', 'Nikolaev']
            for city in cities:
                s = City()
                s.name = city
                s.country = record
                s.save()