from django.db import models
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class Ticket(models.Model):
    title = models.CharField(max_length=254, default='', blank=False)
    summary = models.TextField(blank=False)
    ticket_type = models.CharField(max_length=30, blank=False)
    screenshot = models.ImageField(upload_to="images", blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    creator = models.CharField(max_length=150, blank=False) 
    status = models.CharField(max_length=30, default='Backlog')
    initiation_date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    completion_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return "{0} - {1}".format(self.ticket_type, self.title)