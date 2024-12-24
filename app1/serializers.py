from .models import Customer,Address,Service
from rest_framework import serializers


class ServiceSer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields = ['id','keluhan','tindakan','hasil','service_date','img_url']

class AddressSer(serializers.ModelSerializer):
    services = ServiceSer(many=True, required=False)
    class Meta:
        model=Address
        fields = ['id','address','lat','lng','img_url','services']

class CustomerSer(serializers.ModelSerializer):
    addresses = AddressSer(many=True, required=False)
    class Meta:
        model=Customer
        fields = ['id','name','email','phone','addresses']