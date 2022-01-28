from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}            
    return render(request, 'register.html', context)    