# -*- coding: utf-8 -*- 
from django.forms import ModelForm
from django import forms
from restaurant.widgets import SelectWithPop, MultipleSelectWithPop
from restaurant.models import Contact, Restaurant
from client.models import Video, Branch

class ContactForm(ModelForm):
    class Meta:
        model = Contact

class RestaurantForm(ModelForm):
    contact = forms.ModelChoiceField(Contact.objects.all(), widget=SelectWithPop, label=u'Контакт')
    restriction = forms.ModelMultipleChoiceField(Branch.objects, widget=MultipleSelectWithPop, label=u'Ограничения')
    video = forms.ModelMultipleChoiceField(Video.objects, widget=MultipleSelectWithPop, label=u'Ролик')

    class Meta:
        model = Restaurant
