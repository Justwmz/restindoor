from django.forms import ModelForm
from django import forms
from restaurant.models import Contact, Restaurant

class ContactForm(ModelForm):
    class Meta:
        model = Contact

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
