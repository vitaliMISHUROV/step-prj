from django.shortcuts import render, get_object_or_404
from main.models import Country

def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', {"countries": countries})

def country_info(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    context = {'country': country}
    return render(request, 'country.html', context)
