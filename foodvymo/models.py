from django.db import models

# Create your models here.
class Merchant(models.Model):
    resturantName = models.CharField(max_length=128)
    contactName = models.CharField(max_length=128)
    pincode = models.CharField(max_length=6)
    location = models.CharField(max_length=256)
    website = models.URLField(max_length=128)
    phoneNumber = models.CharField(max_length=13)
    averageDailyTransaction = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.resturantName} {self.contactName} {self.averageDailyTransaction}"