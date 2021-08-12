from django import forms
from . models import Practitioners





class PractitionersForm(forms.ModelForm):
    class Meta:
        model = Practitioners
        fields = ('__all__')