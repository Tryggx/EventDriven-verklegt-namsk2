from django.shortcuts import render, get_object_or_404
from event.models import Event, Show


# Create your views here.
def index(request):
    return render(request, 'event/index.html', context={
        'events':Event.objects.all()
    })

def get_event_by_id(request, eventid):
    return render(request, 'event/single_event.html', {
        'event': get_object_or_404(Event, pk=eventid),
        'shows': Event.objects.get(pk=eventid).show_set.all()
    })

def get_zones_by_showid(request, showid, eventid):
    return render(request, 'event/single_show.html', {
        'event': get_object_or_404(Event, pk=eventid),
        'zones': Show.objects.get(pk=showid).zone_set.all(),
        'show' : get_object_or_404(Show, pk=showid)
    })
