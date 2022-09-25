from django.contrib import admin
from .models import User
from .models import Address
from .models import Product
from .models import Order
from .models import Order_Product
from .models import Category

# Register your models here.

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Product)
admin.site.register(Category)
