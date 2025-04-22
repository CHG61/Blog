# views.py
from django.shortcuts import render
from .models import Dream  # modeli içe aktar

def mydream(request):
    dreams = Dream.objects.all()  # veritabanından tüm hayalleri çek
    return render(request, 'mydream.html', {'dreams': dreams})
