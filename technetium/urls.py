from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'technetium.views.home', name='home'),
    # url(r'^technetium/', include('technetium.foo.urls')),
    url(ur'^login/$', 'django.contrib.auth.views.login'),
    url(ur'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    
    url(ur'^$', 'technetium.views.index'),
    url(ur'^dashboard/$', 'technetium.views.dashboard'),

    url(ur'^invoice/', include('invoice.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(ur'^admin/', include(admin.site.urls)),
)
