from django.contrib import admin

# Register your models here.
from .models import Customer,Address,Service

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Service)
