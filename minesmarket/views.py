# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from trombi.models import UserProfile
from minesmarket.models import Produit, Commande, Achat
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.db.models import Max

@login_required
def catalogue(request):		
	liste_produits = Produit.objects.order_by('categorie', 'nom')
	return render_to_response('minesmarket/catalogue.html', {'liste_produits': liste_produits},context_instance=RequestContext(request))

@login_required
def commande(request):
	try:
		commande = Commande.objects.get(eleve__user__username=request.user.username, fermee=False)
		liste_achats = Achat.objects.filter(commande__id = commande.id)
		total = 0
		for achat in liste_achats:
			total = total + achat.produit.prix_vente*achat.quantite	
	except Commande.DoesNotExist:
		liste_achats = None	
		total = 0
	return render_to_response('minesmarket/commande.html', {'liste_achats': liste_achats, 'total':total},context_instance=RequestContext(request))

@login_required
def acheter(request):
	if request.POST:
		try:
			commande = Commande.objects.get(eleve__user__username=request.user.username, fermee=False)
		except Commande.DoesNotExist:
			commande = Commande.objects.create(eleve = request.user.get_profile())
		
		produit = get_object_or_404(Produit, id = request.POST['id'])
		try:
			achat = Achat.objects.get(commande__id = commande.id, produit__id = produit.id)
			if request.POST['quantite'] == "0":
				achat.delete()
			else:
				achat.quantite = request.POST['quantite']
				achat.save()
		except Achat.DoesNotExist:
			if request.POST['quantite'] != "0":
				achat = Achat.objects.create(commande = commande, produit = produit, quantite = request.POST['quantite'])		
	return redirect('minesmarket.views.commande')

@login_required
def commander(request):
	commande = Commande.objects.get(eleve__user__username=request.user.username, fermee=False) #On recupere la commande dont l'eleve est l'utilisateur qui request la page, qui doit être encore ouverte
	commande.fermee = True #On la ferme
	commande.date_fermeture = datetime.today() #On enregistre la date de fermeture
	commande.save() #On enregistre
	return redirect('minesmarket.views.catalogue')

@login_required
def fermer_commandes(request):
	Commande.objects.filter(fermee = False).update(fermee = True, date_fermeture = datetime.today())
	return redirect('minesmarket.views.catalogue')
	
@login_required
def dernieres_commandes(request):	
	liste_commandes = Commande.objects.filter(date_fermeture = Commande.objects.aggregate(Max('date_fermeture'))['date_fermeture__max'])
	return liste_commandes
	
def dernieres_commandes_csv(request):
	from django.template import loader, Context
	liste_commandes = dernieres_commandes(request)
	date_fermeture = Commande.objects.aggregate(Max('date_fermeture'))['date_fermeture__max']
	response = HttpResponse(mimetype='text/csv; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=dernieres_commandes.csv'

	t = loader.get_template('minesmarket/dernieres_commandes.txt')
	c = Context({'liste_commandes': liste_commandes, 'date_fermeture': date_fermeture})
	response.write(t.render(c))
	return response
	
@login_required
def supprimer_achat(request, id_achat):
	achat = get_object_or_404(Achat, id = id_achat)
	print "achat" + str(achat)
	commande = achat.commande
	if achat.commande.eleve.user == request.user and achat.commande.fermee == False:
		achat.delete()
	print "commande" + str(commande)
	return redirect('minesmarket.views.commande')
	
@login_required
def supprimer_tous_achats(request):
	try:
		commande = Commande.objects.get(eleve__user__username=request.user.username, fermee=False)
		liste_achats = Achat.objects.filter(commande__id = commande.id)
		total = 0
		for achat in liste_achats:
			achat.delete()	
	except Commande.DoesNotExist:
		liste_achats = None	
		total = 0
	return redirect('minesmarket.views.commande')