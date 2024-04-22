from django.db import models
from .hotel import Hotel

class Room(models.Model):
    name = models.CharField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    daily_price = models.DecimalField(decimal_places=2,max_digits=9)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.name} | Hotel: {self.hotel.__repr__()}"
