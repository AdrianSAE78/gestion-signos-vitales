from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def table_patients(request):
    patients = Patient.objects.order_by('last_name')
    context = {
        'patients': patients
    }
    return render(request, 'patients.html', context)