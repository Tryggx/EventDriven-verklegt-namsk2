from django.contrib import admin
from event.models import *
from user.models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Show)
admin.site.register(Zone)
admin.site.register(EventType)
admin.site.register(User)
admin.site.register(Ticket)