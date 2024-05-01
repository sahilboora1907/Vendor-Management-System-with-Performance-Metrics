from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=10, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    po_number = models.CharField(max_length=10, unique=True)
    order_date = models.DateField()
    delivery_date = models.DateField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performance')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.vendor.name + ' - ' + str(self.date)