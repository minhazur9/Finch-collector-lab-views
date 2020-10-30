from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about,name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_details, name='details'),
    path('cars/add/', views.add_car, name='add_car'),
    path('cars/<int:car_id>/add-upgrade',views.add_upgrade, name='add_upgrade'),  
    path('cars/<int:car_id>/delete-car',views.delete_car, name='delete_car'),  
    path('cars/<int:car_id>/assoc-extra/<int:extra_id>',views.assoc_extra, name='assoc_extra'),
    path('cars/<int:car_id>/remove-assoc-extra/<int:extra_id>',views.remove_assoc_extra, name='remove_assoc_extra'),
    path('accounts/signup', views.signup, name='signup'),
]
