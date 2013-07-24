# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from restaurant.views import handlePopAdd
from client.forms import BranchForm, VideoForm


@login_required
def index(request):
    return render_to_response('client/index.html', locals(), context_instance=RequestContext(request))


@login_required
def newBranch(request):
    return handlePopAdd(request, BranchForm, 'restriction', 'popaddbranch.html')


@login_required
def newVideo(request):
    return handlePopAdd(request, VideoForm, 'video', 'popaddvideo.html')
