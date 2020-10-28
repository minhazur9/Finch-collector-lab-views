from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Car

from .forms import AddCarForm

from .forms import AddUpgradeForm

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

def add_car(request):
    add_form = AddCarForm(request.POST)
    return render(request, 'cars/add.html', {'add_form': add_form})


def  create_Car(request):
    form = AddCarForm(request.POST)

    # if form is valid
    if form.is_valid():
        # submit the form
        new_form = form.save(commit=False)
        new_form.save()

    return redirect('index')

def add_upgrade(request,car_id):
    form = AddUpgradeForm(request.POST)

    if form.is_valid():
        # submit the form
        new_form = form.save(commit=False)
        new_form.car_id = car_id
        new_form.save()

    return redirect('details',car_id=car_id)

    


