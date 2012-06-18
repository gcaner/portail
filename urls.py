from django.conf.urls.defaults import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitebde.views.home', name='home'),

    (r'^timetable/', include('timetable.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
    (r'^admin/?', include(admin.site.urls)),
	(r'^token/?$','trombi.views.token'),
    (r'^messages/?$','messages.views.index'),
	(r'^messages/json$','messages.views.index_json'),
    (r'^messages/(?P<message_id>\d+)/$', 'messages.views.detail'),
    (r'^messages/(?P<message_id>\d+)/lire/$', 'messages.views.lire'),
	(r'^messages/(?P<message_id>\d+)/classer_non_lu/$', 'messages.views.classer_non_lu'),
    (r'^messages/(?P<message_id>\d+)/classer_important/$', 'messages.views.classer_important'),
    (r'^messages/(?P<message_id>\d+)/classer_non_important/$', 'messages.views.classer_non_important'),
    (r'^messages/tous/$', 'messages.views.tous'),
    (r'^messages/importants/$', 'messages.views.importants'),
    (r'^associations/$', 'association.views.index'),
    (r'^associations/(?P<association_pseudo>\w+)/$', 'association.views.messages'),
	(r'^associations/(?P<association_pseudo>\w+)/equipe/$', 'association.views.equipe'),
	(r'^associations/(?P<association_pseudo>\w+)/messages/$', 'association.views.messages'),
	(r'^associations/(?P<association_pseudo>\w+)/evenements/$', 'association.views.evenements'),
    (r'^associations/(?P<association_pseudo>\w+)/ajouter_membre/$', 'association.views.ajouter_membre'),
    (r'^associations/(?P<association_pseudo>\w+)/supprimer_membre/$', 'association.views.supprimer_membre'),
	(r'^associations/(?P<association_pseudo>\w+)/poster_message/$', 'messages.views.nouveau'),
	(r'^associations/vendome/nouveau/?$','vendome.views.index'),
	(r'^associations/vendome/page/?$','vendome.views.page'),
	(r'^associations/jump/page/?$','jump.views.index'),
    (r'^people/?$','trombi.views.index'),
    (r'^people/json$','trombi.views.index_json'),
    (r'^people/(?P<mineur_login>\w+)/?$','trombi.views.detail'),
    (r'^people/(?P<mineur_login>\w+)/json$','trombi.views.detail_json'),
    (r'^people/(?P<mineur_login>\w+)/img$','trombi.views.image'),
    (r'^people/(?P<mineur_login>\w+)/thumb$','trombi.views.thumbnail'),
    (r'^people/(?P<mineur_login>\w+)/edit/?$','trombi.views.edit'),    
	(r'^objetstrouves/?$','objettrouve.views.index'),
    (r'^objetstrouves/ajouter/?$','objettrouve.views.ajouter'),
    (r'^objetstrouves/supprimer/?$','objettrouve.views.supprimer'),
    (r'^petitscours/?$','petitscours.views.index'),
    (r'^petitscours/admin/?$','petitscours.views.admin'),
    (r'^petitscours/admin/archive/(?P<page>\d*)/?$','petitscours.views.archive'),
    (r'^petitscours/admin/add/?$','petitscours.views.add'),
    (r'^petitscours/admin/give/(?P<id>\d+)/(?P<mineur_login>\w+)/?$','petitscours.views.give'),
    (r'^petitscours/request/(?P<request_id>\d+)/?$','petitscours.views.add_request'),
	(r'^todo/nouveau/?$','todo.views.nouveau'),
	(r'^todo/xhr_test/?$','todo.views.xhr_test'),
    (r'^recherche/?$','recherche.views.search'),
    (r'^/?$','streamine.views.index'),
    (r'^accounts/profile/$', 'trombi.views.profile'),
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    # (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # (r'^accounts/password/reset/?$', 'django.contrib.auth.views.password_reset'),

)