from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls                import patterns, include, url
from django.conf.global_settings     import STATICFILES_DIRS, DEBUG
from django.conf.urls                import patterns, url, include
import decroly.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('decroly.views',
    # Examples:
    # url(r'^$',        'decroly.views.home', name='home'),
    # url(r'^decroly/', include('decroly.foo.urls')),
    url(r'^$',       'index',  name='index'),
    url(r'^about$',  'about',  name='about'),
    url(r'^login$',  decroly.views.LoginView.as_view(),  name='login'),
    url(r'^logout$', decroly.views.LogoutView.as_view(), name='logout'),
    url(r'', include('data.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


#from decroly.settings import DEBUG
#if DEBUG:
#    urlpatterns += patterns('', (
#        r'^static/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': 'static'}
#    ))

#from decroly.settings import DEBUG, STATIC_ROOT
#if DEBUG:
#    urlpatterns += patterns('', (
#        r'^static/(?P.*)$', 'django.views.static.serve',
#        {'document_root':STATIC_ROOT, 'show_indexes': True}
#    ), )

#if DEBUG:
#    urlpatterns = patterns('',
#        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
#            {'document_root':STATICFILES_DIRS}),
#    )

urlpatterns += staticfiles_urlpatterns()

handler404 = 'decroly.views.custom404'
handler403 = 'decroly.views.custom403'
handler500 = 'decroly.views.custom500'

