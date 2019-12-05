from django.db import models
from add_items.models import *



class Cart(models.Model):
    custom=models.ForeignKey(Pizza_compose, null=True, blank=True, on_delete=models.CASCADE)
    menu=models.ForeignKey(Pizza_menu, null=True, blank=True, on_delete=models.CASCADE)
    total_price=models.FloatField()
    message=models.CharField(max_length=256,null=True, blank=True)
