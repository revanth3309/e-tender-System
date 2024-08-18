from django.db import models

# Create your models here.

class Tender(models.Model):
    tender_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    num_tenders_done = models.IntegerField(default=0)
    license_id = models.CharField(max_length=100)
    license_photo = models.ImageField(upload_to='license_photos/')
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Tender ID: {self.tender_id}, Username: {self.username}"
