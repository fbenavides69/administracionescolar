# -*- coding: utf-8 -*-
from django.http                    import HttpResponse
from django.shortcuts               import render_to_response
from django.conf                    import settings
from django.template                import RequestContext
from django.contrib                 import messages
from django.contrib                 import auth
from django.contrib.auth            import REDIRECT_FIELD_NAME, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms      import AuthenticationForm
from django.utils.decorators        import method_decorator
from django.contrib.auth.tokens     import default_token_generator
from django.contrib.auth.models     import User
from django.core.urlresolvers       import reverse_lazy
from django.http                    import Http404
from django.utils.decorators        import method_decorator
from django.utils.http              import base36_to_int
from django.views.decorators.cache  import never_cache
from django.views.decorators.csrf   import csrf_protect
from django.views.generic.edit      import FormView
from django.views.generic.base      import RedirectView
from django.core.urlresolvers       import reverse
import urlparse

def index(request, template_name='index.html'):
    return render_to_response(template_name,
        context_instance=RequestContext(request))


def about(request, template_name='about.html'):
    return render_to_response(template_name,
        context_instance=RequestContext(request))


class LoginView(FormView):
    form_class          = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name       = 'login.html'

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

    def get_success_url(self):
        #redirect_to = self.request.REQUEST.get(self.redirect_field_name, '')
        #netloc = urlparse.urlparse(redirect_to)[1]
        #if not redirect_to:
        #    redirect_to = settings.LOGIN_REDIRECT_URL
        #elif netloc and netloc != self.request.get_host():
        #    redirect_to = settings.LOGIN_REDIRECT_URL
        #return redirect_to
        return reverse('alumni-lista')


class LogoutView(RedirectView):
    #redirect_field_name = REDIRECT_FIELD_NAME

    def get_redirect_url(self):
        #elf.request.REQUEST.get(self.redirect_field_name, '')
        #if redirect_to:
        #    netloc = urlparse.urlparse(redirect_to)[1]
        #    if netloc and netloc != self.request.get_host():
        #        redirect_to = ''
        #return redirect_to or reverse('login')
        return reverse('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, u'Usted ha salido del sistema')
        return super(LogoutView, self).get(request, *args, **kwargs)

