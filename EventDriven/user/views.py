from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect
from forms.forms import RegisterUserForm, UserEditForm, ChangePasswordForm
from user.models import Ticket
from event.models import Event
User = get_user_model()

def update_user(request):
    instance = get_object_or_404(User, pk=request.user.id)
    editform = UserEditForm(instance=instance)
    passform = ChangePasswordForm(user=request.user)
    context = {
        'editform': editform,
        'passform': passform
    }
    if request.method == "POST":
        if 'editform' in request.POST:
            editform = UserEditForm(data=request.POST, instance=instance)
            if editform.is_valid():
                editform.save()
                return redirect('/users/profile')
        if 'passform' in request.POST:
            passform = ChangePasswordForm(data=request.POST, user=request.user)
            if passform.is_valid():
                passform.save()
                return redirect('/users/profile')
    return render(request, 'user/userprofile.html', context=context)

@login_required
def profile(request):
    return render(request, 'user/userprofile.html', {
        'tickets': Ticket.objects.filter(userid=request.user.id),
        'events': Event.objects.all()
    })



#def change_password(request):
#    if request.method == "POST":
#        form = ChangePasswordForm(data=request.POST, user=request.user )
#        if form.is_valid():
#            form.save()
#            return redirect('/users/profile')
#    else:
#        form = ChangePasswordForm(user = request.user)
#    return render(request, 'user/change_password.html', {
#        "passform": form
#    })
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

