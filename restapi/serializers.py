from rest_framework import serializers
from restapi.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'date_time', 'name', 'description')
