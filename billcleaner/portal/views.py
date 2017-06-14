# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from forms import SignUpForm, ReportForm
from models import Peep

# Create your views here.
@login_required
def home(request):
    name = request.user.username
    profile = get_object_or_404(Peep, username=name)
    return render(request, 'home.html', {'profile': profile})

def report(request):
    if request.method == 'POST':
        name = request.user.username
        profile = get_object_or_404(Peep, username=name)
        form = ReportForm(request.POST, instance=profile)
        form.save()
        return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'report.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})