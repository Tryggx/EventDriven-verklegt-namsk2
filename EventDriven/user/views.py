from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.db.models import Count
from django import forms
from forms.forms import RegisterUserForm, UserEditForm, ChangePasswordForm
from user.models import Ticket, Likes
from event.models import Event, EventType, Show

User = get_user_model()

def update_user(request):
    instance = get_object_or_404(User, pk=request.user.id)
    likes = Likes.objects.filter(userid=request.user.id)
    list = []
    for i in likes:
        list.append(i.likestype_id)
    editform = UserEditForm(instance=instance)
    if request.method == "POST":
        editform = UserEditForm(data=request.POST, instance=instance)
        newlikes = request.POST.getlist('favorite_categories')
        if editform.is_valid():
            editform.save()
            likes.delete()
            for i in newlikes:
                savelikes = Likes()
                savelikes.likestype_id = int(i)
                savelikes.userid_id = request.user.id
                savelikes.save()
            return redirect('/users/profile')
    return render(request, 'user/userprofile.html', {
        'editform': editform
    })

@login_required
def profile(request):
    instance = get_object_or_404(User, pk=request.user.id)
    likes = Likes.objects.filter(userid=request.user.id)
    tickets = Ticket.objects.filter(userid=request.user.id)
    shows = Ticket.objects.values('showid').distinct()
    ticketcountdict = {}
    for show in shows:
        ticketcountdict[show['showid']] = (Ticket.objects.filter(showid=show['showid']).count())
    list = []

    for i in likes:
        list.append(str(i.likestype_id))
    return render(request, 'user/userprofile.html', {
        'tickets': tickets,
        'shows': Show.objects.filter(ticket__userid_id=request.user.id).distinct(),
        'events': Event.objects.all(),
        'editform': UserEditForm(instance=instance, initial={"favorite_categories": list}),
        'likes': Likes.objects.all(),
        'ticketcountdict': ticketcountdict

    })



def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user )
        if form.is_valid():
            form.save()
            return redirect('/users/profile')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'user/change_password.html', {
        "passform": form
    })
def register(request):
    if request.method == 'POST':
        print("POST REQUEST")
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/users/login')
        else:
            messages.info(request, 'invalid registration details')
            return render(
                request, 'user/register.html', {
                    'form': form
                })

    return render(request, 'user/register.html', {
        'form': RegisterUserForm()
        })

