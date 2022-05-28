from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name="login_page"),
    path('profile', views.profile, name='users_profile')
]
