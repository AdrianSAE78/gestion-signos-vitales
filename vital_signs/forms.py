from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta: 
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'middle_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'document_id' : forms.IntegerField(attrs={'class' : 'form-control'}, required=True),
            'birth_date' : forms.DateField(attrs={'class' : 'form-control'}, required=False),
            'age' : forms.IntegerField(attrs={'class' : 'form-control'}, required=False),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'diseases' : forms.Textarea(attrs={'class' : 'form-control'}),
        }