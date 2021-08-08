from django.db import models
from datetime import datetime

# Create your models here.

class Contactus(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    emails = models.CharField(max_length=100, blank=False)
    company_name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=False)
    created_date = models.DateTimeField(blank=True, default=datetime.now)


    def __str__(self):
        return self.full_name