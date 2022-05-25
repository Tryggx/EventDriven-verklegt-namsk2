from django.shortcuts import render, get_object_or_404
from event.models import Event

# Create your views here.
def index(request):
    return render(request, 'event/index.html', context={ 'events':Event.objects.all() })
