from django.contrib import admin
from . models import AddProduct, Contact, Purchase
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone","desc")

class AddProductAdmin(admin.ModelAdmin):
    list_display = ("slno","name","image","stock","price")

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("name","address","phone","email","item","quantity","price","delivery")



admin.site.register(Contact)
admin.site.register(AddProduct)
admin.site.register(Purchase)

