
from django.shortcuts import get_object_or_404
from .models import Customer,Address,Service
from .serializers import CustomerSer,AddressSer,ServiceSer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_api_key.permissions import HasAPIKey

# Create your views here.
class CustomerList(APIView):
    permission_classes = [HasAPIKey]
    def get(self,request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSer(customers, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CustomerSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    permission_classes = [HasAPIKey]
    def get(self,request, pk, format=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSer(customer)
        return Response(serializer.data)       
    def delete(self,request, pk, format=None):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request, pk, format=None): 
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSer(customer, data=request.data, partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressView(APIView):
    permission_classes = [HasAPIKey]
    def post(self,request, format=None):
        serializer = AddressSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressEachView(APIView):
    permission_classes = [HasAPIKey]
    def get(self,request,pk,format=None):
        address= get_object_or_404(Address,pk=pk)
        serializer = AddressSer(address)
        return Response(serializer.data)
    def delete(self,request,pk,format=None):
        address= get_object_or_404(Address,pk=pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request, pk, format=None): 
        address = get_object_or_404(Address, pk=pk)
        serializer = AddressSer(address, data=request.data, partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceView(APIView):
    permission_classes = [HasAPIKey]
    def post(self,request, format=None):
        serializer = ServiceSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ServiceEachView(APIView):
    permission_classes = [HasAPIKey]
    def get(self,request,pk,format=None):
        service=get_object_or_404(Service,pk=pk)
        serializer = ServiceSer(service)
        return Response(serializer.data)
    def delete(self,request,pk,format=None):
        service=get_object_or_404(Service,pk=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request, pk, format=None): 
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSer(service, data=request.data, partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
