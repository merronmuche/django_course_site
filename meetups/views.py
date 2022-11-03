from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()

    return render(request,'meetups/index.html', {
        'show_meetups': True,
        'meetups':meetups})

def base(request):

    return render(request, 'meetups/base.html')