from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    data = {
        'name':'mery',
        'gender': 'M',
        'occupation':'Engineer'
    }
    meetups = [
        {'title':'A First meetup'},
        {'title':'A Second meetup'}
    ]

    return render(request,'meetups/index.html', {
        'show_meetups': False,
        'meetups':meetups
    })
