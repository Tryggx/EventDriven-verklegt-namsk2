from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="event_index"),
    path('<int:eventid>', views.get_event_by_id, name="event_details"),
    path('<int:eventid>/shows/<int:showid>', views.get_zones_by_showid, name="zones")
]
