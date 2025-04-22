from django.shortcuts import render
from .models import HomepageHighlight

def CengizhanGenc(request):
    highlights = HomepageHighlight.objects.all()
    return render(request, 'index.html', {'highlights': highlights})
