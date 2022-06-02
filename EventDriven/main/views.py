from datetime import datetime

from django.db.models import Q, OuterRef, Sum, Count, F
from django.shortcuts import render
from sql_util.aggregates import SubqueryAggregate

from event.models import Event, EventType, Show, Zone
from random import randrange

# Create your views here.


def index(request):
    headliners = Event.objects.filter(headliner=True, show__datetime__gte=datetime.today())
    events = Event.objects.filter(show__datetime__gte=datetime.today()).distinct()
    if headliners.count() != 0:
        headliners_rnd = randrange(headliners.count())
    else:
        headliners = [False]
        headliners_rnd = 0
    return render(request, 'main/front.html', context={
        'events': events,
        'eventtypes': EventType.objects.filter(event__in=events).distinct(),
        'headliners': headliners[headliners_rnd],
        'shows': Show.objects.values().annotate(
            availabletickets=SubqueryAggregate(
                'zone__total_tickets', filter=Q(showid=OuterRef('id')), aggregate=Sum)-Count('ticket')),
        'zones': Zone.objects.values().annotate(availabletickets=F('total_tickets')-Count('ticket'))
    })

#clock = 7
#for i in range(10):
#    NewShow = Show(venueid=Venue.objects.get(pk=3), eventid=Event.objects.get(pk=3), datetime=datetime(2022, 6, 6, clock, 0), seating=1000, accessible_seating=10)
#    NewShow.save()
#    clock = clock+1
