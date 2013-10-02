# -*- coding: utf-8 -*- 
from django.forms import ModelForm
import floppyforms as forms
from restaurant.widgets import PhoneInput
from tech.models import Contact, Device

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'position': forms.TextInput(),
            'characteristic': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'phone_work': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd'}),
            'phone_cell': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd'}),
            'address': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'additional': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
        }

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        widgets = {
            'problems': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
        }
