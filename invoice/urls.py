from django.conf.urls import patterns, url

urlpatterns = patterns('invoice.views',
        url(ur'^generate/(?P<invoice_id>\w+)/key/(?P<key>\w{30})/$', 'generate'),
        url(ur'^$', 'index'),
        url(ur'^create/$', 'create', name="create"),
)
