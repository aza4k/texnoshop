from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to a different page if already logged in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout



def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to a different page if already logged in

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})






