from rest_framework import serializers
from django.urls import reverse
from ..models import Room, Hotel
from .hotel_serializer import HotelSerializer

class HotelSearchSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    city = serializers.StringRelatedField()

    class Meta:
        model = Hotel
        fields = '__all__'

    def get_url(self, hotel):
        return reverse('hotel_detail', args=[hotel.id])

class RoomSearchSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    hotel = HotelSearchSerializer(many=False, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'

    def get_url(self, room):
        return reverse('room_detail', args=[room.hotel_id, room.id])