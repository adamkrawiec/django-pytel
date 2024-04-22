from datetime import datetime

from ...models import Room, Hotel, Booking

class AvailableRoomFinder:
    def __init__(self, check_in, check_out):
        self.check_in = check_in
        self.check_out = check_out

    def _bookings_for_rooms(self, rooms):
        bookings = Booking.objects.filter(room__in=rooms)

        if self.check_in and self.check_out:
            bookings = bookings.filter(check_in__gt=self.check_in, check_out__lt=self.check_out)

        return bookings

    def find_available_rooms_for_city(self, city_name):
        # Find available rooms in a city
        hotels = Hotel.objects.filter(city__name__iexact=city_name).all()
        rooms = Room.objects.prefetch_related('hotel').filter(hotel__in=hotels)
        rooms = rooms.exclude(booking__in=self._bookings_for_rooms(rooms))
        return rooms
    
    def find_available_rooms_for_hotel(self, hotel_id):
        rooms = Room.objects.filter(hotel=hotel_id)
        rooms = rooms.exclude(booking__in=self._bookings_for_rooms(rooms))
        return rooms