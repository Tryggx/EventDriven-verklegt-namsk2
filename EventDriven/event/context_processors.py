

def eventtype_processor(request):
    from event.models import EventType
    return {
        'all_eventtypes': EventType.objects.all()

    }