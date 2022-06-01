from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="event_index"),
    path('<int:eventid>', views.get_event_by_id, name="event_details"),
    path('<int:eventid>/shows/<int:showid>', views.get_zones_by_showid, name="zones"),
    path('eventjson/<int:eventid>', views.eventjson, name="eventjson"),
    path('<int:eventid>/shows/<int:showid>/zones/<int:zoneid>', views.get_zone),
    path('<int:eventid>/shows/<int:showid>/zones/<int:zoneid>/payment', views.confirmticket)


]
