from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Value, IntegerField, F, OuterRef, Sum, Q
from django.db.models.functions import Cast
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from event.models import Event, Show, EventType, Zone
from sql_util.utils import SubqueryAggregate

from forms.forms import PaymentInfoForm
from user.models import Ticket, User

# Create your views here.



def index(request):
    if 'search' in request.GET:
        search_param = request.GET['search']
        events = list(Event.objects.filter(name__icontains=search_param).values())
        return JsonResponse({'data': events})
    return render(request, 'event/index.html', context={
        'events': Event.objects.filter(show__datetime__gte=datetime.today())
    })

def get_event_by_id(request, eventid):
    return render(request, 'event/single_event.html', {
        'event': get_object_or_404(Event, pk=eventid),
        'shows': Show.objects.values().filter(eventid=eventid).annotate(
            availabletickets=SubqueryAggregate(
                'zone__total_tickets', filter=Q(showid=OuterRef('id')), aggregate=Sum)-Count('ticket')),
        'today': datetime.now(),
        'similar_events': Event.objects.filter(eventtypeid=(
            Event.objects.get(pk=eventid).eventtypeid_id),show__datetime__gte=datetime.today()).distinct().exclude(pk=eventid)
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
        'events': Event.objects.filter(eventtypeid=eventtypeid).filter(show__datetime__gte=datetime.today()).distinct()
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

def get_zone(request, eventid, showid, zoneid):
    return render(request, 'event/single_zone.html', {
        'event': Event.objects.get(pk=eventid),
        'show': Show.objects.get(pk=showid),
        'zone': Zone.objects.get(pk=zoneid)
    })

@login_required(login_url='/users/login')
def confirmticket(request, eventid, showid, zoneid):
    if request.method == 'POST':
        #if 'addressform' and 'paymentform' in request.POST:
            #addressform = AddressInfoForm(data=request.POST)
           # paymentform = PaymentForm(data=request.POST)
           # return render(request, 'event/orderconfirmed.html', {
           # 'addressform': addressform,
          #  'paymentform': paymentform
         #   })
        forms = request.POST
        for i in range(int(forms.get('num_tickets'))):
            user = User.objects.get(pk=request.user.id)
            zone = Zone.objects.get(pk=zoneid)
            show = Show.objects.get(pk=showid)
            newTicket = Ticket(showid=show, zone_name=zone, userid=user)
            newTicket.save()
        print('post request from ticketsite')
        return render(request, 'event/orderconfirmed.html', {
            'forms': forms,
            'event': Event.objects.get(pk=eventid),
            'show': Show.objects.get(pk=showid),
            'zone': Zone.objects.get(pk=zoneid)

        })
    return render(request, 'event/payment.html', {
        'event': Event.objects.get(pk=eventid),
        'show': Show.objects.get(pk=showid),
        'zone': Zone.objects.values().annotate(availabletickets=F('total_tickets')-Count('ticket')).filter(showid=showid).get(pk=zoneid),
        'paymentinfoform': PaymentInfoForm()
    })




#Zone.objects.values('id').annotate(Count(Ticket.objects.filter(zone_name_id=id)))

#Zone.objects.values('ticket').annotate(c=Count('ticket'))

#Show.objects.values().annotate(total_tickets_show=SubqueryAggregate(Zone.objects.filter(showid=OuterRef('id')).values('showid').distinct(),aggregate=Sum('zone__total_tickets')))

#Show.objects.values().annotate(total_tickets_show=SubqueryAggregate('zone__total_tickets', filter=Q(showid=OuterRef('id')), aggregate=Sum))

#Zone.objects.values('showid').distinct().annotate(total_show_tickets=Sum('total_tickets')).values('total_show_tickets')