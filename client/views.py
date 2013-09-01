# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from client.models import Client, Contact, AdvertisingCampaign
from client.forms import ClientForm, ContactForm, AdvertisingCampaignForm


@login_required
def index(request):
    clients_all = Client.objects.all()
    clients = Client.objects.all()

    return render_to_response('client/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newClient(request):
    formClient = ClientForm(request.POST or None)
    if formClient.is_valid():
        formClient.save()
        error(request, 'Информация о клиенте успешно добавлена.')
        return redirect('client-index')
    var = {'formClient': formClient}

    return render_to_response('client/client/edit.html', var, context_instance=RequestContext(request))


@login_required
def editClient(request, id):
    client = Client.objects.get(id=id)
    formClient = ClientForm(request.POST or None, instance=client)
    if formClient.is_valid():
        formClient.save()
        error(request, 'Информация о клиенте успешно изменена.')
        return redirect('client-index')
    var = {'client': client, 'formClient': formClient}

    return render_to_response('client/client/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    error(request, 'Информация о ресторане успешно удалена.')

    return redirect('client-index')


@login_required
def indexContact(request):
    contacts = Contact.objects.all()

    return render_to_response('client/contact/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newContact(request):
    formCont = ContactForm(request.POST or None)
    if formCont.is_valid():
        formCont.save()
        error(request, 'Информация о контакте успешно добавлена.')
        return redirect('contact-index')
    var = {'formCont': formCont}

    return render_to_response('client/contact/edit.html', var, context_instance=RequestContext(request))


@login_required
def editContact(request, id):
    contact = Contact.objects.get(id=id)
    formCont = ContactForm(request.POST or None, instance=contact)
    if formCont.is_valid():
        formCont.save()
        error(request, 'Информация о контакте успешно изменена.')
        return redirect('contact-index')
    var = {'contact': contact, 'formCont': formCont}

    return render_to_response('client/contact/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteContact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    error(request, 'Информация о контакте успешно удалена.')

    return redirect('contact-index')


@login_required
def indexAdvertisingCampaign(request):
    acs = AdvertisingCampaign.objects.all()

    return render_to_response('client/ac/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newAdvertisingCampaign(request):
    formAC = AdvertisingCampaignForm(request.POST or None)
    if formAC.is_valid():
        formAC.save()
        error(request, 'Информация о рекламной кампании успешно добавлена.')
        return redirect('ac-index')
    var = {'formAC': formAC}

    return render_to_response('client/ac/edit.html', var, context_instance=RequestContext(request))


@login_required
def editAdvertisingCampaign(request, id):
    ac = AdvertisingCampaign.objects.get(id=id)
    formAC = AdvertisingCampaignForm(request.POST or None, instance=ac)
    if formAC.is_valid():
        formAC.save()
        error(request, 'Информация о рекламной кампании успешно изменена.')
        return redirect('ac-index')
    var = {'ac': ac, 'formAC': formAC}

    return render_to_response('client/ac/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteAdvertisingCampaign(request, id):
    ac = AdvertisingCampaign.objects.get(id=id)
    ac.delete()
    error(request, 'Информация о рекламной кампании успешно удалена.')

    return redirect('ac-index')
