from django.shortcuts import render
from .models import Car
# Create your views here.


def gallery(request):
    car = Car.objects.all()
    return render(request, 'gallery/gallery.html', {'cars': car})
