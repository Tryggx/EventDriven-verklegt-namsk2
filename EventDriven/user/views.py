<<<<<<< Updated upstream
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
=======
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

>>>>>>> Stashed changes

# Create your views here.
def login(request):
    return render(request, 'user/loginpage.html')

<<<<<<< Updated upstream
@login_required
def profile(request):
    return render(request, 'user/userprofile.html')
=======
def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
      'form': UserCreationForm()
    })
>>>>>>> Stashed changes
