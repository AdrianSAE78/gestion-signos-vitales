from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

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