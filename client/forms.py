from django.forms import ModelForm
#from django import forms
import floppyforms as forms
from restaurant.widgets import SelectWithPop, PhoneInput
from client.models import Contact, Client, AdvertisingCampaign, Branch, Details

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
            'username': forms.HiddenInput(),
        }

class DetailsForm(ModelForm):
    class Meta:
        model = Details

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        widgets = {
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width:233px'}),
            'adv_ag': forms.Select(attrs={'style': 'width:247px'}),
            'payer': forms.TextInput(attrs={'style': 'width:233px'}),
            'brand': forms.TextInput(attrs={'style': 'width:233px'}),
            'branch': forms.Select(attrs={'style': 'width:247px'}),
            'notes': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'status': forms.Select(attrs={'style': 'width:247px'}),
            'payer_vat': forms.Select(attrs={'style': 'width:247px'}),
            'details': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'negot_res': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'contact_plan': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'username': forms.HiddenInput(),
        }

class AdvertisingCampaignForm(ModelForm):
    class Meta:
        model = AdvertisingCampaign
