# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from client.models import STATUS, Client, Contact, AdvertisingCampaign, Branch, Details, NegotiationResult, Brand, Payer, AdvertisingAgency
from client.forms import ClientForm, ContactForm, AdvertisingCampaignForm, BranchForm, DetailsForm, NegotiationResultForm, BrandForm, PayerForm, AgencyForm
from datetime import date, timedelta


@login_required
def index(request, page=1):
    manager_list = User.objects.filter(groups__name='Менеджеры')
    branch_list = Branch.objects.all()
    status_list = STATUS

    if request.GET.get('manager'):
        manager_act = int(request.GET['manager'])
        if manager_act == 0:
            client_list_tmp = Client.objects.exclude(username__id=manager_act)
        else:
            client_list_tmp = Client.objects.filter(username__id=manager_act)
    else:
        manager_act = request.user.id
        client_list_tmp = Client.objects.filter(username=request.user)
    if request.GET.get('status'):
        status_act = request.GET['status']
        if status_act == '0':
            client_list_tmp = client_list_tmp.exclude(status=status_act)
        else:
            client_list_tmp = client_list_tmp.filter(status=status_act)
    if request.GET.get('branch'):
        branch_act = int(request.GET['branch'])
        if branch_act == 0:
            client_list_tmp = client_list_tmp.exclude(branch=branch_act)
        else:
            client_list_tmp = client_list_tmp.filter(branch=branch_act)

    today = date.today()
    next_week = today + timedelta(7)
    my_client_list = Client.objects.filter(username=request.user)
    paginator = Paginator(client_list_tmp, 10)
    client_list = paginator.page(page)

    return render_to_response('client/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newClient(request):
    my_client = Client(username=request.user)
    ContactFormSet = inlineformset_factory(Client, Contact, form=ContactForm, can_delete=False, extra=1)
    DetailsFormSet = inlineformset_factory(Client, Details, form=DetailsForm, can_delete=False, max_num=1)
    NegotiationResultFormSet = inlineformset_factory(Client, NegotiationResult, form=NegotiationResultForm, can_delete=False, extra=1)
    BrandFormSet = inlineformset_factory(Client, Brand, form=BrandForm, can_delete=True, extra=1)
    PayerFormSet = inlineformset_factory(Client, Payer, form=PayerForm, can_delete=True, extra=1)
    formClient = ClientForm(request.POST or None, request.FILES or None, instance=my_client)
    formContactSet = ContactFormSet(request.POST or None, instance=my_client)
    formDetailsSet = DetailsFormSet(request.POST or None, instance=my_client)
    formNegotiationResultSet = NegotiationResultFormSet(request.POST or None, instance=my_client)
    formBrandSet = BrandFormSet(request.POST or None, instance=my_client)
    formPayerSet = PayerFormSet(request.POST or None, instance=my_client)
    if formClient.is_valid() and formContactSet.is_valid() and formDetailsSet.is_valid() and formNegotiationResultSet.is_valid() and formBrandSet.is_valid() and formPayerSet.is_valid():
        formClient.save()
        formContactSet.save()
        formDetailsSet.save()
        formNegotiationResultSet.save()
        formBrandSet.save()
        formPayerSet.save()
        error(request, 'Информация о клиенте успешно добавлена.')
        return redirect('client-index')
    var = {'formClient': formClient, 'formContactSet': formContactSet, 'formDetailsSet': formDetailsSet, 'formNegotiationResultSet': formNegotiationResultSet, 'formBrandSet': formBrandSet, 'formPayerSet': formPayerSet}

    return render_to_response('client/client/edit.html', var, context_instance=RequestContext(request))


@login_required
def editClient(request, id):
    my_client = Client.objects.get(id=id)
    neg_results = NegotiationResult.objects.filter(client=my_client)
    ContactFormSet = inlineformset_factory(Client, Contact, form=ContactForm, can_delete=False, extra=1)
    DetailsFormSet = inlineformset_factory(Client, Details, form=DetailsForm, can_delete=False, max_num=1)
    NegotiationResultFormSet = inlineformset_factory(Client, NegotiationResult, form=NegotiationResultForm, can_delete=False, extra=1)
    if Brand.objects.filter(client=my_client):
        BrandFormSet = inlineformset_factory(Client, Brand, form=BrandForm, can_delete=True, extra=0)
    else:
        BrandFormSet = inlineformset_factory(Client, Brand, form=BrandForm, can_delete=True, extra=1)
    if Payer.objects.filter(client=my_client):
        PayerFormSet = inlineformset_factory(Client, Payer, form=PayerForm, can_delete=True, extra=0)
    else:
        PayerFormSet = inlineformset_factory(Client, Payer, form=PayerForm, can_delete=True, extra=1)
    formClient = ClientForm(request.POST or None, request.FILES or None, instance=my_client)
    formContactSet = ContactFormSet(request.POST or None, instance=my_client)
    formDetailsSet = DetailsFormSet(request.POST or None, instance=my_client)
    formNegotiationResultSet = NegotiationResultFormSet(request.POST or None, instance=my_client)
    formBrandSet = BrandFormSet(request.POST or None, instance=my_client)
    formPayerSet = PayerFormSet(request.POST or None, instance=my_client)
    if formClient.is_valid() and formContactSet.is_valid() and formDetailsSet.is_valid() and formNegotiationResultSet.is_valid() and formBrandSet.is_valid() and formPayerSet.is_valid():
        formClient.save()
        formContactSet.save()
        formDetailsSet.save()
        formNegotiationResultSet.save()
        formBrandSet.save()
        formPayerSet.save()
        error(request, 'Информация о клиенте успешно изменена.')
        return redirect('client-index')
    var = {'client': my_client, 'neg_results': neg_results, 'formClient': formClient, 'formContactSet': formContactSet, 'formDetailsSet': formDetailsSet, 'formNegotiationResultSet': formNegotiationResultSet, 'formBrandSet': formBrandSet, 'formPayerSet': formPayerSet}

    if request.user != my_client.username:
        return redirect('client-index')
    else:
        return render_to_response('client/client/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    error(request, 'Информация о клиенте успешно удалена.')

    return redirect('client-index')


@login_required
def indexAgency(request, page=1):
    manager_list = User.objects.all()
    branch_list = Branch.objects.all()
    status_list = STATUS

    if request.GET.get('manager'):
        manager_act = int(request.GET['manager'])
        agency_list_tmp = AdvertisingAgency.objects.filter(username__id=manager_act)
    else:
        agency_list_tmp = AdvertisingAgency.objects.all()

    today = date.today()
    next_week = today + timedelta(7)
    my_agency_list = AdvertisingAgency.objects.filter(username=request.user)
    paginator = Paginator(agency_list_tmp, 10)
    agency_list = paginator.page(page)

    return render_to_response('client/agency/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newAgency(request):
    my_agency = AdvertisingAgency(username=request.user)
    ContactFormSet = inlineformset_factory(AdvertisingAgency, Contact, form=ContactForm, can_delete=False, extra=1)
    DetailsFormSet = inlineformset_factory(AdvertisingAgency, Details, form=DetailsForm, can_delete=False, max_num=1)
    NegotiationResultFormSet = inlineformset_factory(AdvertisingAgency, NegotiationResult, form=NegotiationResultForm, can_delete=False, extra=1)
    BrandFormSet = inlineformset_factory(AdvertisingAgency, Brand, form=BrandForm, can_delete=True, extra=1)
    PayerFormSet = inlineformset_factory(AdvertisingAgency, Payer, form=PayerForm, can_delete=True, extra=1)
    formAgency = AgencyForm(request.POST or None, request.FILES or None, instance=my_agency)
    formContactSet = ContactFormSet(request.POST or None, instance=my_agency)
    formDetailsSet = DetailsFormSet(request.POST or None, instance=my_agency)
    formNegotiationResultSet = NegotiationResultFormSet(request.POST or None, instance=my_agency)
    formBrandSet = BrandFormSet(request.POST or None, instance=my_agency)
    formPayerSet = PayerFormSet(request.POST or None, instance=my_agency)
    if formAgency.is_valid() and formContactSet.is_valid() and formDetailsSet.is_valid() and formNegotiationResultSet.is_valid() and formBrandSet.is_valid() and formPayerSet.is_valid():
        formAgency.save()
        formContactSet.save()
        formDetailsSet.save()
        formNegotiationResultSet.save()
        formBrandSet.save()
        formPayerSet.save()
        error(request, 'Информация о рекламном агенстве успешно добавлена.')
        return redirect('agency-index')
    var = {'formAgency': formAgency, 'formContactSet': formContactSet, 'formDetailsSet': formDetailsSet, 'formNegotiationResultSet': formNegotiationResultSet, 'formBrandSet': formBrandSet, 'formPayerSet': formPayerSet}

    return render_to_response('client/agency/edit.html', var, context_instance=RequestContext(request))


@login_required
def editAgency(request, id):
    my_agency = AdvertisingAgency.objects.get(id=id)
    neg_results = NegotiationResult.objects.filter(agency=my_agency)
    ContactFormSet = inlineformset_factory(AdvertisingAgency, Contact, form=ContactForm, can_delete=False, extra=1)
    DetailsFormSet = inlineformset_factory(AdvertisingAgency, Details, form=DetailsForm, can_delete=False, max_num=1)
    NegotiationResultFormSet = inlineformset_factory(AdvertisingAgency, NegotiationResult, form=NegotiationResultForm, can_delete=False, extra=1)
    try:
        Brand.objects.get(agency=my_agency)
    except Exception, e:
        BrandFormSet = inlineformset_factory(AdvertisingAgency, Brand, form=BrandForm, can_delete=True, extra=1)
    else:
        BrandFormSet = inlineformset_factory(AdvertisingAgency, Brand, form=BrandForm, can_delete=True, extra=0)
    try:
        Payer.objects.get(agency=my_agency)
    except Exception, e:
        PayerFormSet = inlineformset_factory(AdvertisingAgency, Payer, form=PayerForm, can_delete=True, extra=1)
    else:
        PayerFormSet = inlineformset_factory(AdvertisingAgency, Payer, form=PayerForm, can_delete=True, extra=0)
    formAgency = AgencyForm(request.POST or None, request.FILES or None, instance=my_agency)
    formContactSet = ContactFormSet(request.POST or None, instance=my_agency)
    formDetailsSet = DetailsFormSet(request.POST or None, instance=my_agency)
    formNegotiationResultSet = NegotiationResultFormSet(request.POST or None, instance=my_agency)
    formBrandSet = BrandFormSet(request.POST or None, instance=my_agency)
    formPayerSet = PayerFormSet(request.POST or None, instance=my_agency)
    if formAgency.is_valid() and formContactSet.is_valid() and formDetailsSet.is_valid() and formNegotiationResultSet.is_valid() and formBrandSet.is_valid() and formPayerSet.is_valid():
        formAgency.save()
        formContactSet.save()
        formDetailsSet.save()
        formNegotiationResultSet.save()
        formBrandSet.save()
        formPayerSet.save()
        error(request, 'Информация о рекламном агенстве успешно изменена.')
        return redirect('agency-index')
    var = {'agency': my_agency, 'neg_results': neg_results, 'formAgency': formAgency, 'formContactSet': formContactSet, 'formDetailsSet': formDetailsSet, 'formNegotiationResultSet': formNegotiationResultSet, 'formBrandSet': formBrandSet, 'formPayerSet': formPayerSet}

    return render_to_response('client/agency/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteAgency(request, id):
    agency = AdvertisingAgency.objects.get(id=id)
    agency.delete()
    error(request, 'Информация о рекламном агенстве успешно удалена.')

    return redirect('agency-index')


@login_required
def indexContact(request, page=1):
    client_list = Client.objects.all()
    manager_list = User.objects.filter(groups__name='Менеджеры')

    if request.GET.get('manager'):
        manager_act = int(request.GET['manager'])
        contact_list_tmp = Contact.objects.filter(client__username__id=manager_act)
    else:
        contact_list_tmp = Contact.objects.all()

    paginator = Paginator(contact_list_tmp, 10)
    contact_list = paginator.page(page)

    return render_to_response('client/contact/index.html', locals(), context_instance=RequestContext(request))


@login_required
def editContact(request, id):
    contact = Contact.objects.get(id=id)
    formCont = ContactForm(request.POST or None, instance=contact)
    if formCont.is_valid():
        formCont.save()
        error(request, 'Информация о контакте успешно изменена.')
        return redirect('client-contact-index')
    var = {'contact': contact, 'formCont': formCont}

    return render_to_response('client/contact/edit.html', var, context_instance=RequestContext(request))


@login_required
def deleteContact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    error(request, 'Информация о контакте успешно удалена.')

    return redirect('client-contact-index')


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
def indexBranch(request, page=1):
    branch_list_tmp = Branch.objects.all()

    paginator = Paginator(branch_list_tmp, 10)
    branch_list = paginator.page(page)

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


