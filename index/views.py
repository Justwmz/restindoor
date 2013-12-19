# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def index(request):
    manager_group = Group.objects.get(name='Менеджеры').user_set.all()
    director_group = Group.objects.get(name='Руководство').user_set.all()

    return render_to_response('index/index.html', locals(), context_instance=RequestContext(request))

@login_required
def chpass(request):
    errors = dict()
    if request.method == 'POST':
        if not request.POST.get('old_pass', ''):
            errors['old_pass'] = 'enter old password'
        if not request.POST.get('new_pass', ''):
            errors['new_pass'] = 'enter new pass'
        if not request.POST.get('pass_confirmed', ''):
            errors['pass_confirm'] = 'enter confirm'
        if not errors:
            if not request.user.check_password(request.POST['old_pass']):
                errors['wrong_pass'] = 'old password is wrong'
            elif request.POST['new_pass'] == request.POST['pass_confirmed']:
                request.user.set_password(request.POST['new_pass'])
                request.user.save()
                pass_changed = True
            else:
                errors['wrong_confirm'] = 'new != confirm'

    return render_to_response('registration/chpass.html', locals(), context_instance=RequestContext(request))
