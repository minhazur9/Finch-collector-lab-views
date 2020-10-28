from django import forms
from .models import Car
from .models import Upgrades


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name','brand','color','price']

class AddUpgradeForm(forms.ModelForm):
    class Meta:
        model = Upgrades
        fields = ['name', 'price']