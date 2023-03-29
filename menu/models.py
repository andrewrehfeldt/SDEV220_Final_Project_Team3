from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    menuNbr = models.IntegerField()
    dishName = models.CharField(max_length=200)
    dishDescr = models.TextField()
    itemPrice = models.FloatField()
    servSize = models.IntegerField()
    customerOpts = models.CharField(max_length=50)
    effectiveDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.dishName
