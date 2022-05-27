

def eventtype_processor(request):
    from event.models import EventType
    return {
        'eventtypes': EventType.objects.all()
    }