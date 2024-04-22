from django.db import models
from .room import Room

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['room', 'check_in', 'check_out'])
        ]

    def __repr__(self):
        return f"{self.room.__repr__()} | Check-in: {self.check_in} | Check-out: {self.check_out}"