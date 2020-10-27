from django.shortcuts import render

from django.http import HttpResponse

from .models import Car

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html',{"cars": cars})

def cars_details(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html',{"car":car})
