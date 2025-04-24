from django.shortcuts import render
from .models import Education

def myeducationlife(request):
    educations = Education.objects.filter(category='general')
    return render(request, 'myeducationlife.html', {'educations': educations})

def erasmus(request):
    educations = Education.objects.filter(category='erasmus')
    return render(request, 'erasmus.html', {'educations': educations})

def data(request):
    educations = Education.objects.filter(category='data')
    return render(request, 'data.html', {'educations': educations})

def sports(request):
    educations = Education.objects.filter(category='sports')
    return render(request, 'sports.html', {'educations': educations})
