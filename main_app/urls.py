from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about,name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_details, name='details'),
    path('cars/add/', views.add_car, name='add_car'),
    path('cars/create_car/', views.create_Car, name='create-car'),
    path('cars/add-upgrade',views.add_upgrade, name='add-upgrade')
]
