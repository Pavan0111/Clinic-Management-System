from django.db import models
from django.utils import timezone
# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)
SHIFT_CHOICES = (
    ("Day", "Day"),
    ("Night", "Night"),
)
STAFF_CHOICES = (
    ("Nurse", "Nurse"),
    ("Clinical Officer", "Clinical Officer"),
    ("Public Health Officer", "Public Health Officer"),
    ("Cleaner", "Cleaner"),
    ("Security", "Security"),
    ("Driver", "Driver"),
    ("Counselor", "Counselor"),
    ("Nutritionist", "Nutritionist"),
)

class BaseInfo(models.Model):
    id_number = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    

    class Meta:
        abstract = True


class Practitioners(BaseInfo):
    position = models.CharField(max_length=100, choices=STAFF_CHOICES)
    employment_date = models.DateTimeField()
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)

    def __str__(self):
        return self.name