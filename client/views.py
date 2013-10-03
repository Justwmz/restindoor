# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from client.models import Client, Contact, AdvertisingCampaign, Branch, Details, NegotiationResult
from client.forms import ClientForm, ContactForm, AdvertisingCampaignForm, BranchForm, DetailsForm, NegotiationResultForm


@login_required
def index(request):
    managers = User.objects.all()
    if request.GET.get('manager'):
        manager_act = int(request.GET['manager'])
        clients = Client.objects.filter(username__id=manager_act)
    else:
        clients = Client.objects.all()

    return render_to_response('client/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newClient(request):
    my_client = Client(username=request.user)
    ClientFormSet1 = inlineformset_factory(Client, Contact, form=ContactForm, can_delete=False, max_num=1)
    ClientFormSet2 = inlineformset_factory(Client, Details, form=DetailsForm, can_delete=False, max_num=1)
    ClientFormSet3 = inlineformset_factory(Client, NegotiationResult, form=NegotiationResultForm, can_delete=False, max_num=1)
    formClient = ClientForm(request.POST or None, request.FILES or None, instance=my_client)
    formClientSet1 = ClientFormSet1(request.POST or None, instance=my_client)
    formClientSet2 = ClientFormSet2(request.POST or None, instance=my_client)
    formClientSet3 = ClientFormSet3(request.POST or None, instance=my_client)
    if formClient.is_valid() and formClientSet1.is_valid() and formClientSet2.is_valid() and formClientSet3.is_valid():
        formClient.save()
        formClientSet1.save()
        formClientSet2.save()
        formClientSet3.save()
        error(request, 'Информация о клиенте успешно добавлена.')
        return redirect('client-index')
    var = {'formClient': formClient, 'formClientSet1': formClientSet1, 'formClientSet2': formClientSet2, 'formClientSet3': formClientSet3}

    return render_to_response('client/client/edit.html', var, context_instance=RequestContext(request))


@login_required
def editClient(request, id):
    my_client = Client.objects.get(id=id)
    neg_results = NegotiationResult.objects.filter(client=my_client)
    ClientFormSet1 = inlineformset_factory(Client, Contact, form=ContactForm, can_delete=False, max_num=1)
    ClientFormSet2 = inlineformset_factory(Client, Details, form=DetailsForm, can_delete=False, max_num=1)
    ClientFormSet3 = inlineformset_factory(Client, NegotiationResult, form=NegotiationResultForm, can_delete=False, extra=1)
    formClient = ClientForm(request.POST or None, request.FILES or None, instance=my_client)
    formClientSet1 = ClientFormSet1(request.POST or None, instance=my_client)
    formClientSet2 = ClientFormSet2(request.POST or None, instance=my_client)
    formClientSet3 = ClientFormSet3(request.POST or None, instance=my_client)
    if formClient.is_valid() and formClientSet1.is_valid() and formClientSet2.is_valid() and formClientSet3.is_valid():
        formClient.save()
        formClientSet1.save()
        formClientSet2.save()
        formClientSet3.save()
        error(request, 'Информация о клиенте успешно изменена.')
        return redirect('client-index')
    var = {'client': my_client, 'neg_results': neg_results, 'formClient': formClient, 'formClientSet1': formClientSet1, 'formClientSet2': formClientSet2, 'formClientSet3': formClientSet3}

    return render_to_response('client/client/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    error(request, 'Информация о ресторане успешно удалена.')

    return redirect('client-index')


@login_required
def indexContact(request):
    clients = Client.objects.all()
    if request.GET.get('client'):
        client_act = int(request.GET['client'])
        contacts = Contact.objects.filter(client__id=client_act)
    else:
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


@login_required
def indexBranch(request):
    branchs = Branch.objects.all()

    return render_to_response('client/branch/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newBranch(request):
    formBranch = BranchForm(request.POST or None)
    if formBranch.is_valid():
        formBranch.save()
        error(request, 'Информация об отраслях успешно добавлена.')
        return redirect('client-branch-index')
    var = {'formBranch': formBranch}

    return render_to_response('client/branch/edit.html', var, context_instance=RequestContext(request))


@login_required
def editBranch(request, id):
    branch = Branch.objects.get(id=id)
    formBranch = BranchForm(request.POST or None, instance=branch)
    if formBranch.is_valid():
        formBranch.save()
        error(request, 'Информация об отрасли успешно изменена.')
        return redirect('client-branch-index')
    var = {'branch': branch, 'formBranch': formBranch}

    return render_to_response('client/branch/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteBranch(request, id):
    branch = Branch.objects.get(id=id)
    branch.delete()
    error(request, 'Информация об отрасли успешно удалена.')

    return redirect('branch-index')


