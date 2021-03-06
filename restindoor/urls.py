from django.conf.urls import patterns, include, url
from haystack.forms import SearchForm
from haystack.views import SearchView
from client.forms import MySearchForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/login/'}),
    url(r'^chpass/$', 'index.views.chpass'),
    url(r'^$', 'index.views.index', name='index'),

    #url(r'^search/', include('haystack.urls')),
    url(r'^search/$', SearchView(form_class=MySearchForm), name='haystack_search'),

    url(r'^client/$', 'client.views.index', name='client-index'),
    url(r'^client/page(?P<page>\d+)/$', 'client.views.index', name='client-index'),
    url(r'^client/client/add/$', 'client.views.newClient', name='client-new'),
    url(r'^client/client/(?P<id>\d+)/$', 'client.views.editClient', name='client-edit'),
    url(r'^client/client/(?P<id>\d+)/delete/$', 'client.views.deleteClient', name='client-delete'),
    url(r'^client/agency/$', 'client.views.indexAgency', name='agency-index'),
    url(r'^client/agency/add/$', 'client.views.newAgency', name='agency-new'),
    url(r'^client/agency/(?P<id>\d+)/$', 'client.views.editAgency', name='agency-edit'),
    url(r'^client/agency/(?P<id>\d+)/delete/$', 'client.views.deleteAgency', name='agency-delete'),
    url(r'^client/contact/$', 'client.views.indexContact', name='client-contact-index'),
    url(r'^client/contact/page(?P<page>\d+)/$', 'client.views.indexContact', name='client-contact-index'),
    url(r'^client/contact/(?P<id>\d+)/$', 'client.views.editContact', name='client-contact-edit'),
    url(r'^client/contact/(?P<id>\d+)/delete/$', 'client.views.deleteContact', name='client-contact-delete'),
    url(r'^client/ac/$', 'client.views.indexAdvertisingCampaign', name='client-ac-index'),
    url(r'^client/ac/add/$', 'client.views.newAdvertisingCampaign', name='client-ac-new'),
    url(r'^client/ac/(?P<id>\d+)/$', 'client.views.editAdvertisingCampaign', name='client-ac-edit'),
    url(r'^client/ac/(?P<id>\d+)/delete/$', 'client.views.deleteAdvertisingCampaign', name='client-ac-delete'),
    url(r'^client/branch/$', 'client.views.indexBranch', name='client-branch-index'),
    url(r'^client/branch/page(?P<page>\d+)/$', 'client.views.indexBranch', name='client-branch-index'),
    url(r'^client/branch/add/$', 'client.views.newBranch', name='client-branch-new'),
    url(r'^client/branch/(?P<id>\d+)/$', 'client.views.editBranch', name='client-branch-edit'),
    url(r'^client/branch/(?P<id>\d+)/delete/$', 'client.views.deleteBranch', name='client-branch-delete'),

    url(r'^restaurant/$', 'restaurant.views.index', name='restaurant-index'),
    url(r'^restaurant/restaurant/add/$', 'restaurant.views.newRestaurant', name='restaurant-new'),
    url(r'^restaurant/restaurant/(?P<id>\d+)/$', 'restaurant.views.editRestaurant', name='restaurant-edit'),
    url(r'^restaurant/restaurant/(?P<id>\d+)/delete/$', 'restaurant.views.deleteRestaurant', name='restaurant-delete'),
    url(r'^restaurant/contact/$', 'restaurant.views.indexContact', name='contact-index'),
    url(r'^restaurant/contact/add/$', 'restaurant.views.newContact', name='contact-new'),
    url(r'^restaurant/contact/(?P<id>\d+)/$', 'restaurant.views.editContact', name='contact-edit'),
    url(r'^restaurant/contact/(?P<id>\d+)/delete/$', 'restaurant.views.deleteContact', name='contact-delete'),
    url(r'^restaurant/restriction/$', 'restaurant.views.indexRestriction', name='restriction-index'),
    url(r'^restaurant/restriction/add/$', 'restaurant.views.newRestriction', name='restriction-new'),
    url(r'^restaurant/restriction/(?P<id>\d+)/$', 'restaurant.views.editRestriction', name='restriction-edit'),
    url(r'^restaurant/restriction/(?P<id>\d+)/delete/$', 'restaurant.views.deleteRestriction', name='restriction-delete'),

    url(r'^tech/$', 'tech.views.index', name='tech-index'),
    url(r'^tech/restaurant/add/$', 'tech.views.newTech', name='tech-new'),
    url(r'^tech/restaurant/(?P<id>\d+)/$', 'tech.views.editTech', name='tech-edit'),
    url(r'^analytics/$', 'analytics.views.index', name='analytics-index'),
    url(r'^add/contact/?$', 'restaurant.views.newCont'),
)
