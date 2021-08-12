from django.shortcuts import render, HttpResponse

# Create your views here.
def visitors(request):
    return render(request, 'visitors/visitors.html')