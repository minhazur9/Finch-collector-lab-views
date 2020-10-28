from django import forms
from .models import Car
from .models import Upgrade


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name','brand','color','price']

class AddUpgradeForm(forms.ModelForm):
    class Meta:
        model = Upgrade
        fields = ['name', 'price']