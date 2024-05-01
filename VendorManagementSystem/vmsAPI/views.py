from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceDetail(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer