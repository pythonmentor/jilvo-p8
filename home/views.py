from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.conf import settings

# Create your views here.
def home_function(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'index.html')

class LoginView():
    template_name = 'index.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

        return render(request, self.template_name)

class LogoutView():

  template_name = 'front/index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)