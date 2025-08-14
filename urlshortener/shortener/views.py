from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Url
import random
import string


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def home(request):
    recent_urls = None
    if request.user.is_authenticated:
        recent_urls = Url.objects.filter(user=request.user).order_by('-created_at')[:10]

    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            existing = Url.objects.filter(long_url=long_url).first()
            if existing:
                short_code = existing.short_code
            else:
                short_code = generate_short_code()
                while Url.objects.filter(short_code=short_code).exists():
                    short_code = generate_short_code()
                url_obj = Url(long_url=long_url, short_code=short_code)
                if request.user.is_authenticated:
                    url_obj.user = request.user
                url_obj.save()
            short_url = f"{request.build_absolute_uri('/')}{short_code}"
            return render(request, 'shortener/home.html', {'short_url': short_url, 'recent_urls': recent_urls})

    return render(request, 'shortener/home.html', {'recent_urls': recent_urls})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('home')
        else:
            messages.error(request, 'Error during signup. Please check your input.')
    else:
        form = UserCreationForm()
    return render(request, 'shortener/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'shortener/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


def url_redirect(request, short_code):
    url = get_object_or_404(Url, short_code=short_code)
    return redirect(url.long_url)