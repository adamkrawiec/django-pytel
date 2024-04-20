from rest_framework import serializers
from ..models import Booking
from ..bookings.overlaps import BookingOverlaps

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        room_id = self.instance.room_id if self.instance else data.get('room')
        
        if BookingOverlaps().overlapping_bookings(room_id, check_in, check_out).exists():
            raise serializers.ValidationError("Booking overlaps with existing booking for the room.")
        
        return data
