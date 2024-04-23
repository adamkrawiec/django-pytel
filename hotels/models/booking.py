from django.db import models
from .room import Room

class Booking(models.Model):
    class BookingStatus(models.TextChoices):
        PENDING = 'pending'
        CANCELLED = 'cancelled'
        APPROVED = 'approved'
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=BookingStatus.choices,
        default=BookingStatus.PENDING,
    )

    class Meta:
        indexes = [
            models.Index(fields=['room', 'check_in', 'check_out']),
            models.Index(fields=['status']),
        ]
    
    def __repr__(self):
        return f"{self.room.__repr__()} | Check-in: {self.check_in} | Check-out: {self.check_out} | status: {self.status}"