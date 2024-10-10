from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

#-------------Patients---------------

def table_patients(request):
    patients = Patient.objects.order_by('last_name')
    context = {
        'patients': patients
    }
    return render(request, 'patients.html', context)


@login_required
def form_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vital_signs:patients')
    else:
        form = PatientForm()

    return render(request, 'patients_form.html', {'form' : form})

@login_required 
def patients_detail(request, patient_id):
    patients = Patient.objects.get(id = patient_id)
    vital_signs = patients.vital_signs_set.all()
    #vital_signs = Vital_Signs.objects.filter(patient__id = patient_id)
    context = {
        'patients' : patients,
        'vital_signs' : vital_signs
    }
    return render(request, 'patients_detail.html', context)

@login_required 
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk = patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('vital_signs:patients')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients_form.html', {'form' : form})

#-------------Vital Signs---------------

@login_required    
def form_vital_signs(request):
    if request.method == 'POST':
        form = Vital_SignsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('vital_signs:patients')
    else:
        form = Vital_SignsForm()

    return render(request, 'vital_signs_form.html', {'form' : form})


class CustomLoginView(LoginView):
   template_name="login.html"