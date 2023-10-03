from django.contrib import messages
from django.core.mail.backends import console
from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404, redirect
# from .models import



def index(request):
    return render(request, 'home/index.html')
