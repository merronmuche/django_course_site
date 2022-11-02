from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    data = {
        'name':'markos',
        'gender': 'M',
        'occupation':'Engineer'
    }

    return render(request,template_name='meetups/index.html', context=data)
