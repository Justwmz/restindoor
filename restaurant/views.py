# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from django.utils.html import escape
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from restaurant.models import Restaurant, Contact, Restriction, Details
from restaurant.forms import RestaurantForm, ContactForm, RestrictionForm, DetailsForm


@login_required
def index(request):
    managers = User.objects.all()
    if request.GET.get('manager'):
        manager_act = int(request.GET['manager'])
        restaurants = Restaurant.objects.filter(username__id=manager_act)
    else:
        restaurants = Restaurant.objects.all()

    return render_to_response('restaurant/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newRestaurant(request):
    my_restaurant = Restaurant(username=request.user)
    RestaurantFormSet1 = inlineformset_factory(Restaurant, Contact, form=ContactForm, can_delete=False, max_num=1)
    RestaurantFormSet2 = inlineformset_factory(Restaurant, Details, form=DetailsForm, can_delete=False, max_num=1)
    formRest = RestaurantForm(request.POST or None, request.FILES or None, instance=my_restaurant)
    formRestSet1 = RestaurantFormSet1(request.POST or None, instance=my_restaurant)
    formRestSet2 = RestaurantFormSet2(request.POST or None, instance=my_restaurant)
    if formRest.is_valid() and formRestSet1.is_valid() and formRestSet2.is_valid():
        formRest.save()
        formRestSet1.save()
        formRestSet2.save()
        error(request, 'Информация о ресторане успешно добавлена.')
        return redirect('restaurant-index')
    var = {'formRest': formRest, 'formRestSet1': formRestSet1, 'formRestSet2': formRestSet2}

    return render_to_response('restaurant/restaurant/edit.html', var, context_instance=RequestContext(request))


@login_required
def editRestaurant(request, id):
    my_restaurant = Restaurant.objects.get(id=id)
    RestaurantFormSet = inlineformset_factory(Restaurant, Contact, form=ContactForm, can_delete=False, max_num=1)
    formRest = RestaurantForm(request.POST or None, request.FILES or None, instance=my_restaurant)
    formRestSet = RestaurantFormSet(request.POST or None, instance=my_restaurant)
    if formRest.is_valid() and formRestSet.is_valid():
        formRest.save()
        formRestSet.save()
        error(request, 'Информация о ресторане успешно изменена.')
        return redirect('restaurant-index')
    var = {'restaurant': my_restaurant, 'formRest': formRest, 'formRestSet': formRestSet}

    return render_to_response('restaurant/restaurant/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteRestaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.delete()
    error(request, 'Информация о ресторане успешно удалена.')

    return redirect('restaurant-index')


@login_required
def indexContact(request):
    restaurants = Restaurant.objects.all()
    if request.GET.get('restaurant'):
        restaurant_act = int(request.GET['restaurant'])
        contacts = Contact.objects.filter(restaurant__id=restaurant_act)
    else:
        contacts = Contact.objects.all()

    return render_to_response('restaurant/contact/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newContact(request):
    formCont = ContactForm(request.POST or None)
    if formCont.is_valid():
        formCont.save()
        error(request, 'Информация о контакте успешно добавлена.')
        return redirect('contact-index')
    var = {'formCont': formCont}

    return render_to_response('restaurant/contact/edit.html', var, context_instance=RequestContext(request))


@login_required
def editContact(request, id):
    contact = Contact.objects.get(id=id)
    formCont = ContactForm(request.POST or None, instance=contact)
    if formCont.is_valid():
        formCont.save()
        error(request, 'Информация о контакте успешно изменена.')
        return redirect('contact-index')
    var = {'contact': contact, 'formCont': formCont}

    return render_to_response('restaurant/contact/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteContact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    error(request, 'Информация о контакте успешно удалена.')

    return redirect('contact-index')


@login_required
def indexRestriction(request):
    restrictions = Restriction.objects.all()

    return render_to_response('restaurant/restriction/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newRestriction(request):
    formRestrict = RestrictionForm(request.POST or None)
    if formRestrict.is_valid():
        formRestrict.save()
        error(request, 'Информация об ограничениях успешно добавлена.')
        return redirect('restriction-index')
    var = {'formRestrict': formRestrict}

    return render_to_response('restaurant/restriction/edit.html', var, context_instance=RequestContext(request))


@login_required
def editRestriction(request, id):
    restriction = Restriction.objects.get(id=id)
    formRestrict = RestrictionForm(request.POST or None, instance=restriction)
    if formRestrict.is_valid():
        formRestrict.save()
        error(request, 'Информация об ограничении успешно изменена.')
        return redirect('restriction-index')
    var = {'restriction': restriction, 'formRestrict': formRestrict}

    return render_to_response('restaurant/restriction/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteRestriction(request, id):
    restriction = Restriction.objects.get(id=id)
    restriction.delete()
    error(request, 'Информация об ограничении успешно удалена.')

    return redirect('restriction-index')


@login_required
def handlePopAdd(request, addForm, field, templ):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            try:
                newObject = form.save()
            except forms.ValidationError, error:
                newObject = None
            if newObject:
                return HttpResponse('''<script type="text/javascript">
                                            opener.dismissAddAnotherPopup(window, "%s", "%s");
                                        </script>''' % (escape(newObject._get_pk_val()), escape(newObject)))
    else:
        form = addForm()

    pageContext = {'form': form, 'field': field}
    return render_to_response("add/%s" % templ, pageContext, context_instance=RequestContext(request))


@login_required
def newCont(request):
    return handlePopAdd(request, ContactForm, 'contact', 'popaddcontact.html')
