from django.contrib import admin

from .models import *
admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseItem)
admin.site.register(Department)
admin.site.register(Warehouse)
admin.site.register(Employees)
