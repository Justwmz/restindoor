from django.forms import ModelForm
#from django import forms
import floppyforms as forms
from restaurant.widgets import SelectWithPop, PhoneInput
from client.models import Contact, Client, AdvertisingCampaign

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

class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {
            'contact_lvl': forms.Select(attrs={'style': 'width:247px'}),
            'status': forms.Select(attrs={'style': 'width:247px'}),
            'contact_type': forms.Select(attrs={'style': 'width:247px'}),
            'ra': forms.TextInput(attrs={'style': 'width:233px'}),
            'control': forms.Select(attrs={'style': 'width:247px'}),
            'notes': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'tags': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'details': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'contact_result': forms.Textarea(attrs={'style': 'resize:none; width:233px; height:80px'}),
        }

class AdvertisingCampaignForm(ModelForm):
    class Meta:
        model = AdvertisingCampaign
