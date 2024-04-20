from rest_framework import serializers
from django.urls import reverse
from ..models import Room

class RoomSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_url(self, room):
        return reverse('room_detail', args=[room.hotel_id, room.id])