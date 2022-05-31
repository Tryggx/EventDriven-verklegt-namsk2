from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from forms.forms import RegisterUserForm
from user.models import Ticket
from event.models import Event
User = get_user_model()


@login_required
def profile(request):
    return render(request, 'user/userprofile.html', {
        'tickets': Ticket.objects.filter(userid=request.user.id),
        'events': Event.objects.all()
    })


def register(request):
    if request.method == 'POST':
        print("POST REQUEST")
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            print("VALID FORM")
            form.save()
            return redirect('/users/login')

    return render(request, 'user/register.html', {
      'form': RegisterUserForm()
    })
