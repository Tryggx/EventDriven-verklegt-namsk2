from django.urls import path
from . import views
from event import views as eventviews

urlpatterns = [
    path('',views.index, name="main_index"),
    path('concerts', eventviews.allConcerts, name="allConcerts")
]