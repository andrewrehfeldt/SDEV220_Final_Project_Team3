from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_list')
        else:
            messages.success(request, ("Your user name and password didn't match. Please try again"))
            return redirect('login')
    
    else:
        return render(request, 'users/login.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, ("You are logged out now."))
    return redirect('menu_list')

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration is successful"))
            return redirect('menu_list')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'users/profile.html', {'user': user})