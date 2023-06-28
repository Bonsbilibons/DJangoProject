from django import forms
from .models import *


class UploadFileForm(forms.Form):
    class Meta:
        model = Products
        fields = ['name' , 'description' , 'cost' , 'status' , 'amount' , 'icon']