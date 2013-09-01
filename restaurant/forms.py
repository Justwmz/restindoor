# -*- coding: utf-8 -*- 
from django.forms import ModelForm
#from django import forms
import floppyforms as forms
from restaurant.widgets import SelectWithPop, PhoneInput
from restaurant.models import Contact, Restaurant

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'phone_work': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd'}),
            'phone_cell': PhoneInput(attrs={'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd'}),
        }

class RestaurantForm(ModelForm):
#    restriction = forms.ModelMultipleChoiceField(Branch.objects, widget=MultipleSelectWithPop, label=u'Ограничения')
#    video = forms.ModelMultipleChoiceField(Video.objects, widget=MultipleSelectWithPop, label=u'Ролик')

    class Meta:
        model = Restaurant
        widgets = {
            'form_coop': forms.Select(attrs={'style': 'width:247px'}),
            'status': forms.Select(attrs={'style': 'width:247px'}),
            'sum_payment': forms.TextInput(attrs={'style': 'width:197px'}),
            'contact': SelectWithPop,
            'payment_term': forms.Select(attrs={'style': 'width:247px'}),
            'pay_term_com': forms.Textarea(attrs={'style': 'resize:none; width:233px; height:80px'}),
            'details': forms.Textarea(attrs={'style': 'resize:none; height:80px'}),
            'plasma_all': forms.NumberInput(attrs={'style': 'width:40px'}),
            'plasma_work': forms.NumberInput(attrs={'style': 'width:40px'}),
            'restriction': forms.CheckboxSelectMultiple,
            'video': forms.CheckboxSelectMultiple,
            'warranty_mail': forms.Select(attrs={'style': 'width:130px'}),
        }
