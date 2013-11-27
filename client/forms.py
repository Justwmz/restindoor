from django.forms import ModelForm
#from django import forms
import floppyforms as forms
from restaurant.widgets import SelectWithPop, InlineInput
from client.models import Contact, Client, AdvertisingCampaign, Branch, Details, NegotiationResult, Brand, Payer, AdvertisingAgency

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_work': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_cell': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'icq': forms.TextInput(attrs={'class': 'form-control'}),
            'skype': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'style': 'resize:none; height:80px', 'class': 'form-control'}),
            'additional': forms.Textarea(attrs={'style': 'resize:none; height:80px', 'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'brand': InlineInput(attrs={'class': 'form-control'}),
        }

class PayerForm(ModelForm):
    class Meta:
        model = Payer
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'payer': InlineInput(attrs={'class': 'form-control'}),
        }

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'legal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'index': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house1': forms.TextInput(attrs={'class': 'form-control'}),
            'house2': forms.TextInput(attrs={'class': 'form-control'}),
            'room1': forms.TextInput(attrs={'class': 'form-control'}),
            'office': forms.TextInput(attrs={'class': 'form-control'}),
            'room2': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'mfo': forms.TextInput(attrs={'class': 'form-control'}),
            'current_account': forms.TextInput(attrs={'class': 'form-control'}),
            'vat_inn': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'adv_ag': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'style': 'resize:none; height:80px;', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'payer_vat': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class AgencyForm(ModelForm):
    class Meta:
        model = AdvertisingAgency
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'style': 'resize:none; height:80px;', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'payer_vat': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class AdvertisingCampaignForm(ModelForm):
    class Meta:
        model = AdvertisingCampaign
        widgets = {
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class NegotiationResultForm(ModelForm):
    class Meta:
        model = NegotiationResult
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'negot_res': forms.Textarea(attrs={'style': 'resize:none; height:80px;', 'class': 'form-control'}),
            'last_cont_date': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_plan': forms.Textarea(attrs={'style': 'resize:none; height:80px;', 'class': 'form-control'}),
            'next_cont_date': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }
