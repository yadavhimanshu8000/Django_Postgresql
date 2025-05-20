from django.contrib import admin
from myapi.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Shipment)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)

