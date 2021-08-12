from django.shortcuts import render, HttpResponse, redirect
from . models import Practitioners
from . forms import PractitionersForm

# Create your views here.
def practitioners(request):
    return render(request, 'practitioners/practitioners.html')

def practitioners(request):
    practitioners = Practitioners.objects.all()
    return render(request, "practitioners/practitioners.html", {"practitioners": practitioners})
def practitioners_details(request, id):
    practitioners = Practitioners.objects.get(pk=id)
    context = {
        "practitioners": practitioners
    }
    return render(request, "data/practitioners_details.html", context)

def add_practitioners(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PractitionersForm()
        else:
            practitioners = Practitioners.objects.get(pk=id)
            form = PractitionersForm(instance=practitioners)
        return render(request, "practitioners/add_practitioners.html", {"form": form})
    else:
        if id == 0:
            form = PractitionersForm(request.POST)
        else:
            practitioners = Practitioners.objects.get(pk=id)
            form = PractitionersForm(request.POST, instance=practitioners)
        if form.is_valid():
            form.save()
        return redirect('practitioners')