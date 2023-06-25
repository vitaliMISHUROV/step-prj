from django.contrib import admin
from main.models import City, Country
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class  CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(City,CityAdmin)


class CountryAdmin(TranslationAdmin):
       list_display =['name', 'alias']
       list_filter =['name']
       search_fields =['name']

admin.site.register(Country,CountryAdmin)




      

