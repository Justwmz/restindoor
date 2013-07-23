# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from restaurant.models import Restaurant
from restaurant.forms import RestaurantForm, ContactForm


@login_required
def index(request):
    restaurants_all = Restaurant.objects.all()
    if request.GET.get('chain_name_rus'):
        chain_act = request.GET['chain_name_rus']
        restaurants = Restaurant.objects.filter(chain_name_rus__exact=chain_act)
    else:
        restaurants = Restaurant.objects.all()

    return render_to_response('restaurant/index.html', locals(), context_instance=RequestContext(request))


@login_required
def edit(request, id):
    restaurant = Restaurant.objects.get(id=id)
    formRest = RestaurantForm(request.POST or None, instance=restaurant)
    formCont = ContactForm()
    if formRest.is_valid():
        formRest.save()
        return redirect('restaurant-index')
    var = {'restaurant': restaurant, 'formRest': formRest, 'formCont': formCont}

    return render_to_response('restaurant/edit.html', var, context_instance=RequestContext(request))


@login_required
def delete(request, id):
#    restaurant = Restaurant.objects.get(id=id)
#    restaurant.delete()
    error(request, 'Информация о ресторане успешно удалена.')

    return redirect('restaurant-index')
