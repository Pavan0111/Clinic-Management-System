from django.contrib import admin
from . models import Practitioners

# Register your models here.
@admin.register(Practitioners)
class PractitionersAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "position", "shift", "employment_date")