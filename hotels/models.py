from django.db import models
from django.core.exceptions import ValidationError

class City(models.Model):
    name = models.CharField()

class Hotel(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Room(models.Model):
    name = models.CharField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    daily_price = models.DecimalField(decimal_places=2,max_digits=9)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        from .bookings.overlaps import BookingOverlaps
        super().clean()

        if BookingOverlaps().overlapping_bookings(self.room_id, self.check_in, self.check_out).exists():
            raise ValidationError("Booking overlaps with existing booking for the room.")
