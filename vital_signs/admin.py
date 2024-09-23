from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(Vital_Signs)
class Vital_Signs_Admin(admin.ModelAdmin):
    pass