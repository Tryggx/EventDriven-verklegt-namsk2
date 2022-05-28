from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('login',views.login, name="login_page"),
    path('profile', views.profile, name='users_profile')
=======
    path('login', LoginView.as_view(template_name='user/login.html'), name="login_page"),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(next_page='login_page'), name='logout')
>>>>>>> Stashed changes
]
