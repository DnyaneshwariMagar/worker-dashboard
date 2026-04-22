from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import EventSerializer
from django.db.models import Sum
from django.shortcuts import render

@api_view(['POST'])
def add_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "Event added"})
    return Response(serializer.errors)


@api_view(['GET'])
def metrics(request):
    workers = Worker.objects.all()
    data = []

    for w in workers:
        working = Event.objects.filter(worker=w, event_type='working').count()
        idle = Event.objects.filter(worker=w, event_type='idle').count()
        produced = Event.objects.filter(worker=w).aggregate(Sum('count'))

        data.append({
            "name": w.name,
            "working": working,
            "idle": idle,
            "production": produced['count__sum'] or 0
        })

    return Response(data)





def home(request):
    return render(request, 'index.html')