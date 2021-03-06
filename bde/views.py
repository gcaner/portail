#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from trombi.models import UserProfile
from bde.models import Liste, Vote
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required

import datetime

@login_required
# Vote pour une liste
def voter(request):
    debut_vote = None
    fin_vote = None
    peut_voter = False
    deja_vote = False
    liste1 = None
    liste2 = None
    if Liste.objects.filter(debut_vote__gte = datetime.datetime.now()).count() > 0: #Une election va commencer
        debut_vote = (Liste.objects.filter(debut_vote__gte = datetime.datetime.now())[0]).debut_vote
    
    listes = Liste.objects.filter(debut_vote__lte = datetime.datetime.now(), fin_vote__gte = datetime.datetime.now())
    if listes.count() >= 2: #On peut voter
        peut_voter = True
        fin_vote = (Liste.objects.all()[0]).fin_vote
        liste1 = listes[0]
        liste2 = listes[1]        
        if Vote.objects.filter(eleve = request.user.get_profile()).exists(): #L'élève a déjà voté
            # messages.add_message(request, messages.ERROR, "Vous avez déjà voté !")
            peut_voter = False
            deja_vote = True
        elif request.POST:   
            liste = get_object_or_404(Liste, nom = request.POST['choix'])
            Vote.objects.create(liste = liste, eleve=request.user.get_profile())
            messages.add_message(request, messages.INFO, "A voté !")
            peut_voter = False
            deja_vote = True
    return render_to_response('bde/voter.html', {'peut_voter':peut_voter, 'deja_vote':deja_vote, 'liste1':liste1, 'liste2':liste2, 'debut_vote':debut_vote, 'fin_vote':fin_vote}, context_instance=RequestContext(request))
    
@login_required
@permission_required('bde.add_liste')
def resultats(request):
	
    listes = Liste.objects.filter(debut_vote__lte = datetime.datetime.now())
    liste1 = None
    liste2 = None
    if listes.count() >= 2: #Une election est commencée
        liste1 = listes[0]
        liste2 = listes[1]
        n_votes_1 = Vote.objects.filter(liste = liste1).count()
        n_votes_2 = Vote.objects.filter(liste = liste2).count()
    return render_to_response('bde/resultats.html', {'liste1':liste1, 'liste2':liste2, 'n_votes_2':n_votes_2, 'n_votes_1':n_votes_1}, context_instance=RequestContext(request))

def presentation_entreprises(request):
    return render_to_response('bde/presentation_entreprises.html', {}, context_instance=RequestContext(request))

def contact_entreprises(request):
    return render_to_response('bde/contact_entreprises.html', {}, context_instance=RequestContext(request))