from django.db import transaction
from django.db.transaction import get_connection

from ...serializers import BookingSerializer
from ...models import Booking

class BookingCreateAction:
    def __init__(self, room, check_in, check_out):
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
    
    def execute(self):
        booking_params = {}
        booking_params['room'] = self.room
        booking_params['check_in'] = self.check_in
        booking_params['check_out'] = self.check_out
        serializer = BookingSerializer(data=booking_params)
        
        with transaction.atomic():
            cursor = get_connection().cursor()
            cursor.execute(f'LOCK TABLE {Booking._meta.db_table}')
            if serializer.is_valid():
                serializer.save()
            return serializer
