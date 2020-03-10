from django.contrib import admin
from .models import Companies,Products
# Register your models here.


class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['Name','GST']

admin.site.register(Companies,CompaniesAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['Name']


admin.site.register(Products, ProductsAdmin)