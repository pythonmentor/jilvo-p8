from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from .forms import AuthentificationForm, UserRegisterForm


# Create your views here.
def signin_function(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'login.html')

def signup_function(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'signup.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        try:   
            user = User.objects.create_user(username,request.POST["password"],email)
            user.save()
            print(user)
            login(request, user)  # nous connectons l'utilisateur
            messages.success(request, 'Votre compte a bien été crée')
            print("Votre compte a bien été crée")
        except Exception as e:
            form = UserRegisterForm()
            print(e)
            # messages.error("request, 'Votre compte n‘a pas été crée.'")
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def connexion(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        print("déja connecté")
        return redirect('index.html')   
    # if request.method == "GET":
    #     print("Voir la page sans se connecter")
    #     return render(request, 'login.html')
    if request.method == "POST":
        form = AuthentificationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = request.POST["username"]
            print(username)
            password = request.POST["password"]
            print(password)
            user = authenticate(request, username=username, password=password)  # Nous vérifions si les données sont correctes
            print(user)
            if user is not None:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                # return redirect(user_page)
                print("Connecté")
            else: # sinon une erreur sera affichée
                
                print("Utilisateur inconnu ou mauvais de mot de passe.")
    else:
        form = AuthentificationForm()
        print("Rien ne se passe aucune connexion effectué")

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')