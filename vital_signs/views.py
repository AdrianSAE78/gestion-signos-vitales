from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def table_patients(request):
    patients = Patient.objects.order_by('last_name')
    context = {
        'patients': patients
    }
    return render(request, 'patients.html', context)

def form_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vital_signs:patients')
    else:
        form = PatientForm()

    return render(request, 'patients_form.html', {'form' : form})
    
def form_vital_signs(request):
    if request.method == 'POST':
        form = Vital_SignsForm(request.POST)
        if form.is_valid():
            form.save_m2m()
            return redirect('vital_signs:patients')
    else:
        form = Vital_SignsForm()

    return render(request, 'vital_signs_form.html', {'form' : form})