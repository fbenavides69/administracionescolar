from django.conf.urls import patterns, url 
import views

urlpatterns = patterns('',
    url(r'^lista/$',                             views.AlumniList.as_view(),               name = 'alumni-lista'),
    url(r'^lista/(?P<pk>\d+)$',                  views.AlumniRedirectMostrar.as_view(),    name = 'alumni-redirect-mostrar'),
    url(r'^mostrar/(?P<pk>\d+)$',                views.AlumniRetrieve.as_view(),           name = 'alumni-mostrar'),
    url(r'^inscripcion/$',                       views.AlumniRegister.as_view(),           name = 'alumni-inscripcion'),
    url(r'^inscripcion/padres/(?P<pk>\d+)$',     views.AlumniRegisterPadres.as_view(),     name = 'alumni-inscripcion-padres'),
    url(r'^inscripcion/autorizado/(?P<pk>\d+)$', views.AlumniRegisterAutorizado.as_view(), name = 'alumni-inscripcion-autorizado'),
    url(r'^inscripcion/finanzas/(?P<pk>\d+)$',   views.AlumniRegisterFinanzas.as_view(),   name = 'alumni-inscripcion-finanzas'),
    url(r'^inscripcion/documentos/(?P<pk>\d+)$', views.AlumniRegisterDocumentos.as_view(), name = 'alumni-inscripcion-documentos'),
    url(r'^actualizar/alumno/(?P<pk>\d+)$',      views.AlumniUpdateAlumno.as_view(),       name = 'alumni-actualizar-alumno'),
    url(r'^actualizar/padres/(?P<pk>\d+)$',      views.AlumniUpdatePadres.as_view(),       name = 'alumni-actualizar-padres'),
    url(r'^actualizar/autorizado/(?P<pk>\d+)$',  views.AlumniUpdateAutorizado.as_view(),   name = 'alumni-actualizar-autorizado'),
    url(r'^actualizar/finanzas/(?P<pk>\d+)$',    views.AlumniUpdateFinanzas.as_view(),     name = 'alumni-actualizar-finanzas'),
    url(r'^actualizar/documentos/(?P<pk>\d+)$',  views.AlumniUpdateDocumentos.as_view(),   name = 'alumni-actualizar-documentos'),
    url(r'^borrar/(?P<pk>\d+)$',                 views.AlumniDelete.as_view(),             name = 'alumni-borrar'),
    )
