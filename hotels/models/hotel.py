from django.db import models
from .city import City

class Hotel(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.name} | City: {self.city.name}"