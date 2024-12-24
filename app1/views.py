
from django.shortcuts import get_object_or_404
from .models import Customer,Address,Service
from .serializers import CustomerSer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CustomerList(APIView):
    def get(self, request, format=None):
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
    def get(self, request, pk, format=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSer(customer)
        return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)