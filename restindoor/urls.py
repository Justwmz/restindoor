from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/login/'}),
    url(r'^$', 'index.views.index'),
    url(r'^chpass/$', 'index.views.chpass'),
    url(r'^client/$', 'client.views.index'),
    url(r'^restaurant/$', 'restaurant.views.index', name='restaurant-index'),
    url(r'^restaurant/(?P<id>\d+)/$', 'restaurant.views.edit'),
    url(r'^restaurant/(?P<id>\d+)/delete/$', 'restaurant.views.delete'),
    url(r'^analytics/$', 'analytics.views.index'),
    url(r'^add/contact/?$', 'restaurant.views.newContact'),
    url(r'^add/restriction/?$', 'client.views.newBranch'),
    url(r'^add/video/?$', 'client.views.newVideo'),
)
