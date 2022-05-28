from django.urls import path
from . import views
from event import views as eventviews

urlpatterns = [
    path('',views.index, name="main_index"),
    path('eventtypes/<int:eventtypeid>', eventviews.get_event_by_type, name="EventByType")
]