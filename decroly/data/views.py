# -*- coding: utf-8 -*-
# Create your views here
from django.views.generic.list   import ListView
from django.views.generic.base   import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit   import CreateView
from django.views.generic.edit   import UpdateView
from django.views.generic.edit   import DeleteView
from django.core.urlresolvers    import reverse
from braces.views                import LoginRequiredMixin
import models
import forms


class AlumniList(LoginRequiredMixin, ListView):
    model                = models.Alumni
    queryset             = model.objects.all()
    context_object_name  = 'alumnos'
    paginate_by          = '25'
    template_name        = 'alumni_list.html'


class AlumniRedirectMostrar(LoginRequiredMixin, RedirectView):
    def get(self, request, *args, **kwargs):
        model     = models.Alumni
        alumni_id = self.kwargs.get('pk', None)
        alumni    = model.objects.get(pk=alumni_id)
        self.url  = '/mostrar/%s' % alumni.id
        return super(AlumniRedirectMostrar, self).get(request, *args, **kwargs)


class AlumniRetrieve(LoginRequiredMixin, DetailView):
    model               = models.Alumni
    context_object_name = 'alumno'
    template_name       = 'alumni_retrieve.html'


class AlumniRetrievePadres(LoginRequiredMixin, DetailView):
    model               = models.Alumni
    context_object_name = 'alumno'
    template_name       = 'alumni_retrieve_parents.html'


class AlumniRetrieveAutorizado(LoginRequiredMixin, DetailView):
    model               = models.Alumni
    context_object_name = 'alumno'
    template_name       = 'alumni_retrieve_authorized.html'


class AlumniRetrieveFinanzas(LoginRequiredMixin, DetailView):
    model               = models.Alumni
    context_object_name = 'alumno'
    template_name       = 'alumni_retrieve_finance.html'


class AlumniRetrieveDocumentos(LoginRequiredMixin, DetailView):
    model               = models.Alumni
    context_object_name = 'alumno'
    template_name       = 'alumni_retrieve_docs.html'


class AlumniRegister(LoginRequiredMixin, CreateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegister
    context_object_name = 'alumno'
    template_name       = 'alumni_register.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-padres', kwargs={'pk':self.object.id})


class AlumniRegisterPadres(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterParents
    context_object_name = 'alumno'
    template_name       = 'alumni_register_parents.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-autorizado', kwargs={'pk':self.object.id})


class AlumniRegisterAutorizado(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterAuthorized
    context_object_name = 'alumno'
    template_name       = 'alumni_register_authorized.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-finanzas', kwargs={'pk':self.object.id})


class AlumniRegisterFinanzas(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterFinance
    context_object_name = 'alumno'
    template_name       = 'alumni_register_finance.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-documentos', kwargs={'pk':self.object.id})


class AlumniRegisterDocumentos(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterDocs
    context_object_name = 'alumno'
    template_name       = 'alumni_register_docs.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-mostrar', kwargs={'pk':self.object.id})


class AlumniUpdate(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegister
    context_object_name = 'alumno'
    template_name       = 'alumni_update.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar', kwargs={'pk':self.object.id})


class AlumniUpdatePadres(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterParents
    context_object_name = 'alumno'
    template_name       = 'alumni_update_parents.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-padres', kwargs={'pk':self.object.id})


class AlumniUpdateAutorizado(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterAuthorized
    context_object_name = 'alumno'
    template_name       = 'alumni_update_authorized.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-autorizado', kwargs={'pk':self.object.id})


class AlumniUpdateFinanzas(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterFinance
    context_object_name = 'alumno'
    template_name       = 'alumni_update_finance.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-finanzas', kwargs={'pk':self.object.id})


class AlumniUpdateDocumentos(LoginRequiredMixin, UpdateView):
    model               = models.Alumni
    form_class          = forms.AlumniFormRegisterDocs
    context_object_name = 'alumno'
    template_name       = 'alumni_update_docs.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-documentos', kwargs={'pk':self.object.id})


class AlumniDelete(LoginRequiredMixin, DeleteView):
    model               = models.Alumni
    context_object_name = 'alumno'
    template_name       = 'alumni_delete.html'
    def get_success_url(self, **kwargs):
        return reverse('alumni-lista')
