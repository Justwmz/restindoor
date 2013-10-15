from django.forms import ModelForm
#from django import forms
import floppyforms as forms
from restaurant.widgets import SelectWithPop, PhoneInput, InlineInput
from client.models import Contact, Client, AdvertisingCampaign, Branch, Details, NegotiationResult, Brand, Payer, AdvertisingAgency

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'position': forms.TextInput(),
            'characteristic': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'phone_work': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(ddd) ddd-dd-dd'}),
            'phone_cell': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(ddd) ddd-dd-dd'}),
            'address': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'additional': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'brand': InlineInput(),
        }

class PayerForm(ModelForm):
    class Meta:
        model = Brand
        widgets = {
            'client': forms.HiddenInput(),
            'agency': forms.HiddenInput(),
            'payer': InlineInput(),
        }

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        widgets = {
            'code': forms.TextInput(attrs={'style': 'width:85px', 'maxlength': '10'}),
            'index': forms.TextInput(attrs={'style': 'width:138px', 'maxlength': '10'}),
            'region': forms.TextInput(attrs={'style': 'width:166px'}),
            'city': forms.TextInput(attrs={'style': 'width:178px'}),
            'street': forms.TextInput(attrs={'style': 'width:164px'}),
            'house1': forms.TextInput(attrs={'style': 'width:167px'}),
            'house2': forms.TextInput(attrs={'style': 'width:150px'}),
            'room1': forms.TextInput(attrs={'style': 'width:90px'}),
            'office': forms.TextInput(attrs={'style': 'width:85px'}),
            'room2': forms.TextInput(attrs={'style': 'width:85px'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        widgets = {
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width:233px'}),
            'adv_ag': forms.Select(attrs={'style': 'width:247px'}),
            'branch': forms.Select(attrs={'style': 'width:247px'}),
            'notes': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'status': forms.Select(attrs={'style': 'width:247px'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class AgencyForm(ModelForm):
    class Meta:
        model = AdvertisingAgency
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width:233px'}),
            'branch': forms.Select(attrs={'style': 'width:247px'}),
            'notes': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'status': forms.Select(attrs={'style': 'width:247px'}),
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
            'negot_res': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'contact_plan': forms.Textarea(attrs={'style': 'resize:none; height:80px; width:233px'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }
