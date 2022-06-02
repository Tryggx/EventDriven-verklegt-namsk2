from datetime import datetime

from django.db.models import Q, OuterRef, Sum, Count, F
from django.shortcuts import render
from sql_util.aggregates import SubqueryAggregate

from event.models import Event, EventType, Show, Zone
from random import randrange

# Create your views here.


def index(request):
    headliners = Event.objects.filter(headliner=True, show__datetime__gte=datetime.today())
    if headliners.count() != 0:
        headliners_rnd = randrange(headliners.count())
    else:
        headliners = [False]
        headliners_rnd = 0
    return render(request, 'main/front.html', context={
        'events': Event.objects.filter(show__datetime__gte=datetime.today()),
        'eventtypes': EventType.objects.all(),
        'headliners': headliners[headliners_rnd],
        'shows': Show.objects.values().annotate(
            availabletickets=SubqueryAggregate(
                'zone__total_tickets', filter=Q(showid=OuterRef('id')), aggregate=Sum)-Count('ticket')),
        'zones': Zone.objects.values().annotate(availabletickets=F('total_tickets')-Count('ticket'))
    })
