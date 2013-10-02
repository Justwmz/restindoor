# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from django.utils.html import escape
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from restaurant.models import Restaurant
from tech.models import Contact, Device
from restaurant.forms import RestaurantForm
from tech.forms import ContactForm, DeviceForm


@login_required
def index(request):
    managers = User.objects.all()
    if request.GET.get('manager'):
        manager_act = int(request.GET['manager'])
        restaurants = Restaurant.objects.filter(username__id=manager_act)
    else:
        restaurants = Restaurant.objects.all()

    return render_to_response('tech/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newTech(request):
    my_restaurant = Restaurant(username=request.user)
    RestaurantFormSet1 = inlineformset_factory(Restaurant, Contact, form=ContactForm, can_delete=False, max_num=1)
    RestaurantFormSet2 = inlineformset_factory(Restaurant, Device, form=DeviceForm, can_delete=False, max_num=1)
    formRest = RestaurantForm(request.POST or None, request.FILES or None, instance=my_restaurant)
    formRestSet1 = RestaurantFormSet1(request.POST or None, instance=my_restaurant)
    formRestSet2 = RestaurantFormSet2(request.POST or None, instance=my_restaurant)
    if formRest.is_valid() and formRestSet1.is_valid() and formRestSet2.is_valid():
        formRest.save()
        formRestSet1.save()
        formRestSet2.save()
        error(request, 'Информация о ресторане успешно добавлена.')
        return redirect('tech-index')
    var = {'formRest': formRest, 'formRestSet1': formRestSet1, 'formRestSet2': formRestSet2}

    return render_to_response('tech/restaurant/edit.html', var, context_instance=RequestContext(request))


@login_required
def editTech(request, id):
    my_restaurant = Restaurant.objects.get(id=id)
    RestaurantFormSet1 = inlineformset_factory(Restaurant, Contact, form=ContactForm, can_delete=False, max_num=1)
    RestaurantFormSet2 = inlineformset_factory(Restaurant, Device, form=DeviceForm, can_delete=False, max_num=1)
    formRest = RestaurantForm(request.POST or None, request.FILES or None, instance=my_restaurant)
    formRestSet1 = RestaurantFormSet1(request.POST or None, instance=my_restaurant)
    formRestSet2 = RestaurantFormSet2(request.POST or None, instance=my_restaurant)
    if formRest.is_valid() and formRestSet1.is_valid() and formRestSet2.is_valid():
        formRest.save()
        formRestSet1.save()
        formRestSet2.save()
        error(request, 'Информация о ресторане успешно изменена.')
        return redirect('tech-index')
    var = {'restaurant': my_restaurant, 'formRest': formRest, 'formRestSet1': formRestSet1, 'formRestSet2': formRestSet2}

    return render_to_response('tech/restaurant/edit.html', var, context_instance=RequestContext(request))

