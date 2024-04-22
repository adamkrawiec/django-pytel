from django.db import models

class City(models.Model):
    name = models.CharField()

    def __repr__(self):
        return self.name