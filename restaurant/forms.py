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
            'restaurant': forms.Select(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'style': 'width:200px', 'maxlength': '150', 'class': 'form-control'}),
            'position': forms.Select(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'characteristic': forms.Textarea(attrs={'style': 'resize:none; height:80px', 'class': 'form-control'}),
            'phone_work': PhoneInput(attrs={'style': 'width:200px', 'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd', 'class': 'form-control'}),
            'phone_cell': PhoneInput(attrs={'style': 'width:200px', 'class': 'bfh-phone', 'data-format': '(0dd) ddd-dd-dd', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'style': 'width:200px', 'class': 'form-control'}),
            'icq': forms.TextInput(attrs={'style': 'width:200px', 'maxlength': '15', 'class': 'form-control'}),
            'skype': forms.TextInput(attrs={'style': 'width:200px', 'maxlength': '50', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'style': 'resize:none; height:80px', 'class': 'form-control'}),
            'additional': forms.Textarea(attrs={'style': 'resize:none; height:80px', 'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        widgets = {
            'legal_name': forms.TextInput(attrs={'style': 'width:150px', 'maxlength': '10', 'class': 'form-control'}),
            'code': forms.TextInput(attrs={'style': 'width:250px', 'maxlength': '10', 'class': 'form-control'}),
            'index': forms.TextInput(attrs={'style': 'width:138px', 'maxlength': '10', 'class': 'form-control'}),
            'region': forms.TextInput(attrs={'style': 'width:166px', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'style': 'width:178px', 'class': 'form-control'}),
            'street': forms.TextInput(attrs={'style': 'width:164px', 'class': 'form-control'}),
            'house1': forms.TextInput(attrs={'style': 'width:167px', 'class': 'form-control'}),
            'house2': forms.TextInput(attrs={'style': 'width:150px', 'class': 'form-control'}),
            'room1': forms.TextInput(attrs={'style': 'width:90px', 'class': 'form-control'}),
            'office': forms.TextInput(attrs={'style': 'width:85px', 'class': 'form-control'}),
            'room2': forms.TextInput(attrs={'style': 'width:85px', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'style': 'width:150px', 'maxlength': '10', 'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'style': 'width:150px', 'maxlength': '10', 'class': 'form-control'}),
            'mfo': forms.NumberInput(attrs={'style': 'width:150px', 'maxlength': '10', 'class': 'form-control'}),
            'current_account': forms.NumberInput(attrs={'style': 'width:150px', 'maxlength': '10', 'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class RestrictionForm(ModelForm):
    class Meta:
        model = Restriction
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width:150px', 'maxlength': '50', 'class': 'form-control'}),            
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }

class RestaurantForm(ModelForm):
#    restriction = forms.ModelMultipleChoiceField(Branch.objects, widget=MultipleSelectWithPop, label=u'Ограничения')
#    video = forms.ModelMultipleChoiceField(Video.objects, widget=MultipleSelectWithPop, label=u'Ролик')

    class Meta:
        model = Restaurant
        widgets = {
            'name_rus': forms.TextInput(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'name_eng': forms.TextInput(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'chain_name_rus': forms.TextInput(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'chain_name_eng': forms.TextInput(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'rest_open': forms.TextInput(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'rest_close': forms.TextInput(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'site': forms.TextInput(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'broadcast': forms.Select(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'city': forms.Select(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'style': 'resize:none; width:233px; height:80px', 'class': 'form-control'}),
            'form_coop': forms.Select(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'org_form': forms.Select(attrs={'style': 'width:200px', 'class': 'form-control'}),
            'status': forms.Select(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'sum_payment': forms.TextInput(attrs={'style': 'width:97px', 'id': 'sum_1', 'class': 'form-control'}),
            'sum_payment_min': forms.TextInput(attrs={'style': 'width:63px', 'id': 'sum_2', 'class': 'form-control'}),
            'payment_term': forms.Select(attrs={'style': 'width:247px', 'class': 'form-control'}),
            'pay_term_com': forms.Textarea(attrs={'style': 'resize:none; width:233px; height:80px', 'class': 'form-control'}),
            'details': forms.Textarea(attrs={'style': 'resize:none; height:80px', 'class': 'form-control'}),
            'plasma_all': forms.NumberInput(attrs={'style': 'width:100px', 'class': 'form-control'}),
            'plasma_work': forms.NumberInput(attrs={'style': 'width:100px', 'class': 'form-control'}),
            'restriction': forms.CheckboxSelectMultiple,
            'video': forms.CheckboxSelectMultiple,
            'warranty_mail': forms.Select(attrs={'style': 'width:130px', 'class': 'form-control'}),
            'username': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
        }
