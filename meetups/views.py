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
        {
           'title':'A First meetup',
           'location':'new york','slug':
           'a_first_meetup'
        },
        {
            'title':'A Second meetup',
            'location':'paris','slug':
            'a_second_meetup'
        }
    ]

    return render(request,'meetups/index.html', {
        'show_meetups': True,
        'meetups':meetups})
