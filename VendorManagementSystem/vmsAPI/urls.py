from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', VendorList.as_view(), name='vendors'),
    path('vendors/<int:pk>/', VendorDetail.as_view(), name='vendor_detail'),
    path('purchase_orders/', PurchaseOrderList.as_view(), name='purchase_orders'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetail.as_view(), name='purchase_order_detail'),
    path('vendors/<int:pk>/performance', HistoricalPerformanceDetail.as_view(), name='historical_performance_detail'),
]