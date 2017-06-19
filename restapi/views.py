from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi.models import Event
from restapi.serializers import EventSerializer


# Create your views here.
@api_view(['GET'])
def event_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        events = Event.objects.all()
        event_serializer = EventSerializer(events, many=True)
        return Response(event_serializer.data)
