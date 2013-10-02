# -*- coding: utf-8 -*- 
from django.forms import ModelForm
#from django import forms
import floppyforms as forms
from restaurant.widgets import SelectWithPop, PhoneInput
from restaurant.models import Contact, Restaurant, Restriction, Details

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'characteristic': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'phone_work': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd'}),
            'phone_cell': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd'}),
            'address': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'additional': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        widgets = {
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class RestrictionForm(ModelForm):
    class Meta:
        model = Restriction
        widgets = {
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class RestaurantForm(ModelForm):
#    restriction = forms.ModelMultipleChoiceField(Branch.objects, widget=MultipleSelectWithPop, label=u'Ограничения')
#    video = forms.ModelMultipleChoiceField(Video.objects, widget=MultipleSelectWithPop, label=u'Ролик')

    class Meta:
        model = Restaurant
        widgets = {
            'rest_open': forms.TextInput(attrs={'style': 'width:71px'}),
            'rest_close': forms.TextInput(attrs={'style': 'width:71px'}),
            'broadcast': forms.Select(attrs={'style': 'width:247px'}),
            'city': forms.Select(attrs={'style': 'width:247px'}),
            'address': forms.Textarea(attrs={'style': 'resize:none; width:233px; height:80px'}),
            'form_coop': forms.Select(attrs={'style': 'width:247px'}),
            'status': forms.Select(attrs={'style': 'width:247px'}),
            'sum_payment': forms.TextInput(attrs={'style': 'width:79px', 'id': 'sum_1'}),
            'sum_payment_min': forms.TextInput(attrs={'style': 'width:30px', 'id': 'sum_2'}),
            'payment_term': forms.Select(attrs={'style': 'width:247px'}),
            'pay_term_com': forms.Textarea(attrs={'style': 'resize:none; width:233px; height:80px'}),
            'details': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'plasma_all': forms.NumberInput(attrs={'style': 'width:40px'}),
            'plasma_work': forms.NumberInput(attrs={'style': 'width:40px'}),
            'restriction': forms.CheckboxSelectMultiple,
            'video': forms.CheckboxSelectMultiple,
            'warranty_mail': forms.Select(attrs={'style': 'width:130px'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }
