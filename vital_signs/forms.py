from django import forms
from .models import *
from django.forms.widgets import DateInput, Select

class PatientForm(forms.ModelForm):
    class Meta: 
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'middle_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'document_id' : forms.NumberInput(attrs={'class':'form-control', 'type':'text', 'maxlength':'10'}),
            'birth_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'onChange':'calculateAge();'}, format='%Y-%m-%d'),
            'age' : forms.NumberInput(attrs={'class':'form-control', 'type':'text', 'readonly':'readonly'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'diseases' : forms.Textarea(attrs={'class':'form-control'}),
        }

class Vital_SignsForm(forms.ModelForm):
    class Meta:
        model = Vital_Signs
        fields = '__all__'
        widgets = {
            'systolic_blood_pressure' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Sistólica', 'onChange':'bloodPressureLevel();'}),
            'diastolic_blood_pressure' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Diastólica', 'onChange':'bloodPressureLevel();'}),
            'temperature' : forms.NumberInput(attrs={'class':'form-control', 'onChange':'temperatureLevel();'}),
            'heart_Rate' : forms.NumberInput(attrs={'class':'form-control', 'onChange':'heartRateLevel();'}),
            'weight' : forms.NumberInput(attrs={'class':'form-control', 'onChange':'calcIMC();'}),
            'height' : forms.NumberInput(attrs={'class':'form-control', 'onChange':'calcIMC();'}),
            'body_mass_index' : forms.NumberInput(attrs={'class':'form-control', 'readonly':'readonly', 'onChange':'massIndexLevel();'}),
            'patient' : forms.Select(attrs={'class':'form-select patient_select2'}),
        }
    
    def __init__(self, *args, **kwargs ):
        super(Vital_SignsForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all()