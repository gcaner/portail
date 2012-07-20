# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from petitscours.models import PetitCours
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib import messages
def cours_list():
	return PetitCours.objects.filter(visible=True).order_by('date_added')

@login_required
def index(request):
	cours_list = PetitCours.objects.filter(visible=True).order_by('date_added')
	return render_to_response('petitscours/index.html',{'cours_list': cours_list},context_instance=RequestContext(request))

@login_required
def add_request(request,request_id):
	pc = PetitCours.objects.get(id=request_id)
	pc.requests.add(request.user)
	messages.add_message(request, messages.INFO, "C'est bien noté. Yapuka soudoyer le VP petits cours")

	return HttpResponseRedirect('/petitscours/')

@permission_required('petitscours.change_petitcours')
def admin(request):
	cours_list = PetitCours.objects.filter(visible=True).order_by('-date_added')
	archive_list = PetitCours.objects.order_by('-date_given').filter(visible=False)[:3]
	return render_to_response('petitscours/admin.html',{'cours_list': cours_list,'archive_list': archive_list},context_instance=RequestContext(request))

@login_required
def archive(request,page):
	page = int('0'+page)
	next = page+1
	previous = max(page-1,0)
	archive_list = PetitCours.objects.order_by('-date_given').filter(visible=False)[page*10:page*10+10]
	return render_to_response('petitscours/archive.html',{'archive_list': archive_list,'previous':previous,'next':next},context_instance=RequestContext(request))

@login_required
def give(request,id,mineur_login):
	pc = PetitCours.objects.get(id=id)
	pc.date_given = datetime.now()
	pc.visible = False
	pc.save()
	#send_mail('Attribution petit cours', 'Salut ! Tu viens de remporter le petit cours '+pc.title+'.\nPour le contacter: '+pc.contact+'.\nNiveau: '+pc.niveau+'\nMatiere: '+pc.matiere+'\nLieu: '+pc.address+'\nAutre: '+pc.description, '11sibue@ensmp.fr',[mineur_login+'@ensmp.fr'])
	
	return HttpResponseRedirect('/petitscours/admin')

@login_required
def add(request):
	if request.method == 'POST':
		pc = PetitCours()
		pc.title=request.POST['title']
		pc.address=request.POST['address']
		pc.update_location(float(request.POST['lat']), float(request.POST['lng']))
		pc.contact=request.POST['contact']
		pc.matiere = request.POST['matiere']
		pc.niveau = request.POST['niveau']
		pc.description=request.POST['description']
		pc.save()
		if request.is_ajax():
			return HttpResponse("OK")
		else:
			return redirect('/petitscours/admin')
	else:
		return render_to_response('petitscours/add.html',context_instance=RequestContext(request))
