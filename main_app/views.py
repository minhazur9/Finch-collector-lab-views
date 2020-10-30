from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import *

from .forms import AddCarForm,AddUpgradeForm

from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {"cars": cars})


@login_required
def cars_details(request, car_id):
    car = Car.objects.get(id=car_id)
    extras_car_doesnt_have = Extra.objects.exclude(id__in = car.extras.all().values_list('id'))
    add_upgrade = AddUpgradeForm()
    return render(request, 'cars/details.html', {
        "car": car,
        "add_upgrade": add_upgrade,
        "extras": extras_car_doesnt_have
    })

@login_required
def add_car(request):
    if request.method == 'POST':
        add_form = AddCarForm(request.POST)
        if add_form.is_valid():
            new_form = add_form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('index')
        else:     
            add_form = AddCarForm()
            return render(request, 'cars/add.html', {'add_form': add_form})

@login_required
def add_upgrade(request, car_id):
    form = AddUpgradeForm(request.POST)

    if form.is_valid():
        # submit the form
        new_form = form.save(commit=False)
        new_form.car_id = car_id
        new_form.save()

    return redirect('details', car_id=car_id)

@login_required
def delete_car(request, car_id):
    car = Car.objects.get(id=car_id).delete()

    return redirect('index')

@login_required
def assoc_extra(request, car_id, extra_id):
    car = Car.objects.get(id=car_id)
    extra = Extra.objects.get(id=extra_id)
    car.extras.add(extra)
    return redirect('details', car_id=car_id)

@login_required
def remove_assoc_extra(request, car_id, extra_id):
    car = Car.objects.get(id=car_id)
    extra = car.extras.get(id=extra_id)
    car.extras.remove(extra)
    return redirect('details', car_id=car_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)