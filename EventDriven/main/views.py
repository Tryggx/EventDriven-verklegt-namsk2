from django.shortcuts import render
from event.models import Event, EventType
from random import randrange

# Create your views here.


def index(request):
    headliners = Event.objects.filter(headliner=True)
    headliners_rnd = randrange(headliners.count())
    return render(request, 'main/front.html', context={
        'events': Event.objects.all(),
        'eventtypes': EventType.objects.all(),
        'headliners': headliners[headliners_rnd]
    })
