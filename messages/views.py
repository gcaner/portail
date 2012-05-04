#-*- coding: utf-8 -*-
from messages.models import Message
from trombi.models import UserProfile
from association.models import Association, Adhesion
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q


@login_required
def index(request):
	#list_messages = Message.objects.all()
	list_messages = Message.objects.filter(Q(destinataire__isnull=True) | Q(destinataire__in=request.user.get_profile().association_set.all())).exclude(lu__user__username=request.user.username).exclude(important__user__username=request.user.username).order_by('-date')
	return render_to_response('messages/index.html', {'list_messages': list_messages},context_instance=RequestContext(request))
	
@login_required
def detail(request, message_id):
	m = get_object_or_404(Message, pk=message_id)
	#list_commentaires = Commentaire.objects.filter(message=m)
	return render_to_response('messages/detail.html', {'message': m},context_instance=RequestContext(request))
	
@login_required
def lire(request, message_id, no_cache):
	m = get_object_or_404(Message, pk=message_id)	
	m.lu.add(request.user.get_profile())
	m.save()
	
	return render_to_response('messages/action.html', {'message': m})
	
@login_required
def classer_important(request, message_id, no_cache):
	m = get_object_or_404(Message, pk=message_id)
	m.important.add(request.user.get_profile())
	m.save()
	
	return render_to_response('messages/action.html', {'message': m})
	
def classer_non_important(request, message_id, no_cache):
	m = get_object_or_404(Message, pk=message_id)
	m.important.remove(request.user.get_profile())
	m.lu.add(request.user.get_profile())
	m.save()
	
	return render_to_response('messages/action.html', {'message': m})
	
@login_required
def tous(request):

	list_messages = Message.objects.filter(Q(destinataire__isnull=True) | Q(destinataire__in=request.user.get_profile().association_set.all())).order_by('-date')
	return render_to_response('messages/tous.html', {'list_messages': list_messages},context_instance=RequestContext(request))

@login_required
def importants(request):
	list_messages = Message.objects.filter(Q(destinataire__isnull=True) | Q(destinataire__in=request.user.get_profile().association_set.all())).filter(important__user__username=request.user.username).order_by('-date')
	return render_to_response('messages/importants.html', {'list_messages': list_messages},context_instance=RequestContext(request))