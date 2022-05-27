from django.shortcuts import render
from event.models import Event

# Create your views here.


def index(request):
    return render(request, 'front.html', context={
        'events': Event.objects.all()
    })
