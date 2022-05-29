from django.db.models import Count, Value, IntegerField, F
from django.db.models.functions import Cast
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from event.models import Event, Show, EventType, Zone
from user.models import Ticket

# Create your views here.



def index(request):
    return render(request, 'event/index.html', context={
        'events':Event.objects.all()
    })

def get_event_by_id(request, eventid):
    return render(request, 'event/single_event.html', {
        'event': get_object_or_404(Event, pk=eventid),
        'shows': Show.objects.values().annotate(availabletickets=F('seating')+F('accessible_seating')-Count('ticket')).filter(eventid=eventid)
    })

def get_zones_by_showid(request, showid, eventid):
    return render(request, 'event/single_show.html', {
        'event': get_object_or_404(Event, pk=eventid),
        'zones': Zone.objects.values().annotate(availabletickets=F('total_tickets')-Count('ticket')).filter(showid=showid),
        'show': get_object_or_404(Show, pk=showid)
    })

def get_event_by_type(request, eventtypeid):
    return render(request, 'event/index.html', context={
        'header_name': EventType.objects.get(pk=eventtypeid),
        'events': Event.objects.filter(eventtypeid=eventtypeid)
    })

def eventjson(request, eventid):
    singleevent = Event.objects.get(pk=eventid)
    event = {
            'id': singleevent.id,
            'name': singleevent.name,
            'description': singleevent.description,
            'poster_image': singleevent.poster_image,
            'header_image': singleevent.header_image,
            'eventtypeid': singleevent.eventtypeid.id,
            'headliner': singleevent.headliner
    }
    return JsonResponse({'data': event})

#Zone.objects.values('id').annotate(Count(Ticket.objects.filter(zone_name_id=id)))

#Zone.objects.values('ticket').annotate(c=Count('ticket'))