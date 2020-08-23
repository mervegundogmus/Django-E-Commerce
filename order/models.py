from django.contrib.auth.models import User
from property.models import Property
from django.db import models

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.property.title


