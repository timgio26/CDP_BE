from .models import Customer,Address,Service
from rest_framework import serializers


class ServiceSer(serializers.ModelSerializer):
    address_id = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(),source='address', write_only=True)
    class Meta:
        model=Service
        fields = ['address_id','id','keluhan','tindakan','hasil','service_date','img_url']

class AddressSer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)
    services = ServiceSer(many=True, required=False)
    class Meta:
        model=Address
        fields = ['customer_id','id','address','lat','lng','img_url','services']

class CustomerSer(serializers.ModelSerializer):
    addresses = AddressSer(many=True, required=False)
    class Meta:
        model=Customer
        fields = ['id','name','email','phone','addresses']