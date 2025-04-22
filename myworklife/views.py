# views.py
from django.shortcuts import render
from .models import WorkExperience

def myworklife(request):
    works = WorkExperience.objects.filter(category='worklife')
    return render(request, 'myworklife.html', {'works': works})

def mycv(request):
    cvs = WorkExperience.objects.filter(category='cv')
    return render(request, 'mycv.html', {'cvs': cvs})

def Dataanalyst(request):
    analysts = WorkExperience.objects.filter(category='dataanalyst')
    return render(request, 'Dataanalyst.html', {'analysts': analysts})
