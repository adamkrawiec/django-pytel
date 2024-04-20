from rest_framework import serializers
from django.urls import reverse
from .room_serializer import RoomSerializer
from .city_serializer import CitySerializer
from ..models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, read_only=True)
    rooms = RoomSerializer(many=True, read_only=True, source="room_set")
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = Hotel
        fields = '__all__'

    def get_url(self, hotel):
        return reverse('hotel_detail', args=[hotel.id])