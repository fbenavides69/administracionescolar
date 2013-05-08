from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^lista/$',                             views.AlumniList.as_view(),               name='alumni-lista'),
    url(r'^lista/(?P<pk>\d+)$',                  views.AlumniRedirectMostrar.as_view(),    name='alumni-redirect-mostrar'),
    url(r'^mostrar/(?P<pk>\d+)$',                views.AlumniRetrieve.as_view(),           name='alumni-mostrar'),
    url(r'^mostrar/padres/(?P<pk>\d+)$',         views.AlumniRetrievePadres.as_view(),     name='alumni-mostrar-padres'),
    url(r'^mostrar/autorizado/(?P<pk>\d+)$',     views.AlumniRetrieveAutorizado.as_view(), name='alumni-mostrar-autorizado'),
    url(r'^mostrar/finanzas/(?P<pk>\d+)$',       views.AlumniRetrieveFinanzas.as_view(),   name='alumni-mostrar-finanzas'),
    url(r'^mostrar/documentos/(?P<pk>\d+)$',     views.AlumniRetrieveDocumentos.as_view(), name='alumni-mostrar-documentos'),
    url(r'^inscripcion/$',                       views.AlumniRegister.as_view(),           name='alumni-inscripcion'),
    url(r'^inscripcion/padres/(?P<pk>\d+)$',     views.AlumniRegisterPadres.as_view(),     name='alumni-inscripcion-padres'),
    url(r'^inscripcion/autorizado/(?P<pk>\d+)$', views.AlumniRegisterAutorizado.as_view(), name='alumni-inscripcion-autorizado'),
    url(r'^inscripcion/finanzas/(?P<pk>\d+)$',   views.AlumniRegisterFinanzas.as_view(),   name='alumni-inscripcion-finanzas'),
    url(r'^inscripcion/documentos/(?P<pk>\d+)$', views.AlumniRegisterDocumentos.as_view(), name='alumni-inscripcion-documentos'),
    url(r'^actualizar/(?P<pk>\d+)$',             views.AlumniUpdate.as_view(),             name='alumni-actualizar'),
    url(r'^actualizar/padres/(?P<pk>\d+)$',      views.AlumniUpdatePadres.as_view(),       name='alumni-actualizar-padres'),
    url(r'^actualizar/autorizado/(?P<pk>\d+)$',  views.AlumniUpdateAutorizado.as_view(),   name='alumni-actualizar-autorizado'),
    url(r'^actualizar/finanzas/(?P<pk>\d+)$',    views.AlumniUpdateFinanzas.as_view(),     name='alumni-actualizar-finanzas'),
    url(r'^actualizar/documentos/(?P<pk>\d+)$',  views.AlumniUpdateDocumentos.as_view(),   name='alumni-actualizar-documentos'),
    url(r'^borrar/(?P<pk>\d+)$',                 views.AlumniDelete.as_view(),             name='alumni-borrar'),
)
