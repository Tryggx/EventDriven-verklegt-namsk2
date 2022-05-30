from django.db.models import Q, OuterRef, Sum, Count, F
from django.shortcuts import render
from sql_util.aggregates import SubqueryAggregate

from event.models import Event, EventType, Show, Zone
from random import randrange

# Create your views here.


def index(request):
    headliners = Event.objects.filter(headliner=True)
    headliners_rnd = randrange(headliners.count())
    return render(request, 'main/front.html', context={
        'events': Event.objects.all(),
        'eventtypes': EventType.objects.all(),
        'headliners': headliners[headliners_rnd],
        'shows': Show.objects.values().annotate(
            availabletickets=SubqueryAggregate(
                'zone__total_tickets', filter=Q(showid=OuterRef('id')), aggregate=Sum)-Count('ticket')),
        'zones': Zone.objects.values().annotate(availabletickets=F('total_tickets')-Count('ticket'))
    })
