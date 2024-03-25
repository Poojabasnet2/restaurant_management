from django.contrib import admin
from .models import Menu, Inventory,Order,Recipe



# Register your models here.
admin.site.register(Menu)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(Recipe)