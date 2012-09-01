from django.conf.urls.defaults import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitebde.views.home', name='home'),

    (r'^timetable/', include('timetable.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	(r'^static/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')}),
	    
    (r'^admin/?', include(admin.site.urls)),
	(r'^token/$','trombi.views.token'),
    (r'^messages/$','messages.views.index'),
	(r'^messages/json/$','messages.views.index_json'),
    (r'^messages/(?P<message_id>\d+)/$', 'messages.views.detail'),
    (r'^messages/(?P<message_id>\d+)/lire/$', 'messages.views.lire'),
	(r'^messages/(?P<message_id>\d+)/classer_non_lu/$', 'messages.views.classer_non_lu'),
    (r'^messages/(?P<message_id>\d+)/classer_important/$', 'messages.views.classer_important'),
    (r'^messages/(?P<message_id>\d+)/classer_non_important/$', 'messages.views.classer_non_important'),
    (r'^messages/tous/$', 'messages.views.tous'),
    (r'^messages/importants/$', 'messages.views.importants'),
	(r'^associations/mediamines/', include('mediamines.urls')),
	(r'^associations/minesmarket/catalogue/$','minesmarket.views.catalogue'),
	(r'^associations/minesmarket/commande/$','minesmarket.views.commande'),
	(r'^associations/minesmarket/acheter/$','minesmarket.views.acheter'),
	(r'^associations/minesmarket/fermer_commandes/$','minesmarket.views.fermer_commandes'),
	(r'^associations/minesmarket/dernieres_commandes/$','minesmarket.views.dernieres_commandes_csv'),
	(r'^associations/jump/$', 'jump.views.etudes'),	
	(r'^associations/jump/etudes/$', 'jump.views.etudes'),
	(r'^associations/vendome/nouveau/$','vendome.views.nouveau'),
	(r'^associations/vendome/archives/$','vendome.views.archives'),
	(r'^associations/vendome/archives/json/$','vendome.views.archives_json'),
	(r'^associations/wei/teaser/$',direct_to_template, {'template': 'wei/teaser.html'}),
    (r'^associations/$', 'association.views.index'),	
    (r'^associations/(?P<association_pseudo>\w+)/$', 'association.views.messages'),
	(r'^associations/(?P<association_pseudo>\w+)/equipe/$', 'association.views.equipe'),
	(r'^associations/(?P<association_pseudo>\w+)/equipe/changer_ordre/$', 'association.views.changer_ordre'),	
	(r'^associations/(?P<association_pseudo>\w+)/equipe/ajouter_membre/$', 'association.views.ajouter_membre'),
    (r'^associations/(?P<association_pseudo>\w+)/equipe/supprimer_membre/$', 'association.views.supprimer_membre'),
	(r'^associations/(?P<association_pseudo>\w+)/messages/$', 'association.views.messages'),
	(r'^associations/(?P<association_pseudo>\w+)/messages/poster_message/$', 'messages.views.nouveau'),
	(r'^associations/(?P<association_pseudo>\w+)/evenements/$', 'association.views.evenements'),
	(r'^associations/(?P<association_pseudo>\w+)/evenements/nouveau/$', 'evenement.views.nouveau'),	
	(r'^associations/(?P<association_pseudo>\w+)/evenements/(?P<evenement_id>\d+)/$', 'evenement.views.consulter_billetterie'),
	(r'^associations/(?P<association_pseudo>\w+)/evenements/(?P<evenement_id>\d+)/resa', 'evenement.views.confirmer_billetterie'),
	(r'^billetterie/?', 'evenement.views.billetterie_globale'),
    (r'^people/?$','trombi.views.index'),
    (r'^people/avatar/', include('avatar.urls')),	
    (r'^people/json/$','trombi.views.index_json'),
    (r'^people/(?P<mineur_login>\w+)/?$','trombi.views.detail'),
    (r'^people/(?P<mineur_login>\w+)/json/$','trombi.views.detail_json'),
    (r'^people/(?P<mineur_login>\w+)/img/$','trombi.views.image'),
    (r'^people/(?P<mineur_login>\w+)/thumb/$','trombi.views.thumbnail'),
    (r'^people/(?P<mineur_login>\w+)/edit/?$','trombi.views.edit'),   
	(r'^calendrier/$', 'evenement.views.index'),
	(r'^calendrier/json/$', 'evenement.views.index_json'),
	(r'^calendrier/nouveau/$', 'evenement.views.nouveau_calendrier'),
	(r'^calendrier/supprimer/$', 'evenement.views.supprimer_calendrier'),
	(r'^calendrier/update/$', 'evenement.views.update_calendrier'),
	(r'^objetstrouves/?$','objettrouve.views.index'),
    (r'^objetstrouves/ajouter/?$','objettrouve.views.ajouter'),
    (r'^objetstrouves/supprimer/?$','objettrouve.views.supprimer'),
    (r'^petitscours/?$','petitscours.views.index'),
    (r'^petitscours/admin/?$','petitscours.views.admin'),
    (r'^petitscours/admin/archive/(?P<page>\d*)/?$','petitscours.views.archive'),
    (r'^petitscours/admin/add/?$','petitscours.views.add'),
    (r'^petitscours/admin/give/(?P<id>\d+)/(?P<mineur_login>\w+)/?$','petitscours.views.give'),
    (r'^petitscours/request/(?P<request_id>\d+)/?$','petitscours.views.add_request'),
	(r'^petitscours/json/?$','petitscours.views.index_json'),
	(r'^todo/nouveau/?$','todo.views.nouveau'),
	(r'^todo/(?P<id_note>\d+)/supprimer/?$','todo.views.supprimer'),
	(r'^sondages/voter/?$','sondages.views.voter'),
	(r'^sondages/proposer/?$','sondages.views.proposer'),
	(r'^sondages/valider/?$','sondages.views.valider'),
	(r'^sondages/supprimer/?$','sondages.views.supprimer'),
	(r'^sondages/(?P<indice_sondage>\d+)/json/?$','sondages.views.detail_json'),	
    (r'^recherche/?$','recherche.views.search'),    
    (r'^accounts/profile/$', 'trombi.views.profile'),
    (r'^accounts/', include('django.contrib.auth.urls')),
	(r'^comments/post/$', 'messages.views.post_comment' ),
	(r'^comments/delete/$', 'messages.views.delete_own_comment' ),
    (r'^comments/', include('django.contrib.comments.urls')),
	(r'^notifications/$', 'notification.views.liste'),
	(r'^notifications/preferences/$', 'notification.views.preferences'),
	(r'^tinymce/', include('tinymce.urls')),
	(r'^/?$','messages.views.index'),
    # (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # (r'^accounts/password/reset/?$', 'django.contrib.auth.views.password_reset'),

)

urlpatterns += patterns('',url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)