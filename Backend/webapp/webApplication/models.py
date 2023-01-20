from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class HotelUser(models.Model):
    username = models.CharField(max_length=100)
    # image = models.BinaryField()
    image = models.CharField(max_length=1000000)

