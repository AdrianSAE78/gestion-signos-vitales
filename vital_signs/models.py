import datetime
from django.db import models

# Create your models here.

class Patient (models.Model):
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    document_id = models.IntegerField(unique=True, null=False)
    birth_date = models.DateField(null=False)
    age = models.IntegerField(null=False)
    phone = models.CharField(max_length=15, null=True)
    diseases = models.TextField(max_length=350, null=True)

    def __str__(self) -> str:
        return f'{self.last_name} {self.middle_name} {self.first_name}'
    

class Vital_Signs (models.Model):
    date = models.DateField(auto_now_add=True)
    systolic_blood_pressure = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    diastolic_blood_pressure = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    heart_Rate = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    body_mass_index = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f'{self.patient} - {self.blood_pressure}'

