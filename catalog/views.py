import requests

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from .models import Product, Category, UserFavorite

# Create your views here.
def home_function(request):
    # all_entries = Entry.objects.filter(name="Julien")
    # print(all_entries)
    return render(request,"index.html")

def searchresult(request):
    """search the product, if we find product with a name who 
    contains the string of the query we disp 6 product 
    if not we disp 10 product of the base """
    query = request.GET.get('query','')
    print(query)

    if not query:
        title = "Aucun champ rempli, affichage des 10 premiers produits"
        product = Product.objects.all()[0:10]
        context = {
            'product' : product,
            'title': title
        }
    else:
        product = Product.objects.filter(name__contains=query)[:6]
        # cat = Category.product.all()

        if not product:
            title = "Votre recherche n'a donné aucun résultat, affichage des 10 premiers produits"
            product = Product.objects.all()[0:10]
            context ={
                'title': title,
                'product': product
            }
        else:
            title = "Votre recherche est : "
            context = {
                'title': title,
                'product': product
            }
    print(product)
    # print(cat)
    # return render(request,"search_result.html",context)
    return render(request,"search_result.html",context)

def choosen_product(request):
    """ display the detail page for the product """
    query = request.GET.get('product_name','')
    print(query)
    product = Product.objects.get(name=query)
    print(product)
    lst_cat= []
    # cat = Product.category.all()
    for cat in product.category.all(): 
        print(cat)
        lst_cat.append(cat)
    # cat = Category.objects.get(name=product.cat)
    sub_product = Product.objects.filter(category=lst_cat[0]).order_by("nutrition_grade")[:6]
    print(type(sub_product))
    list_cat_order=[]
    # for prod in Product.objects.order_by("")
    
    context = {
        'product': product,
        'sub_product': sub_product
        }
    print(sub_product)
    return render(request,"choosen_product.html",context)

# def substitute(request):
#     """ print the list of 6 substitute for the User """
#     product = Product.objects.filter(category='256')[:6]
#     return render(request,"choosen_product.html",{'product': product})

@login_required
def add_favorite(request):
    """Add the product selected in the list of favorite of the user"""
    print("La fonction pour ajouté un produit est appelé")
    query = request.GET.get('_substitute_product','')
    query_favorite = query
    print(query_favorite)
    print("ID DU PRODUIT")
    username = request.user.id
    user = User.objects.get(id=username)
    print(user)
    print("ID DE L'USER")
    if query_favorite is not None:
        try: 
            UserFavorite.objects.get(user_name=user, product=query_favorite)
            print("Ce produit est déjà dans vos favoris.")
        except ObjectDoesNotExist:
            new_favorite = UserFavorite.objects.create(user_name=username,product=query_favorite)
            new_favorite.save()
            print("Le produit a bien été enregistré.")
    else:
        pass
    return HttpResponse(http_result_message)
    return redirect('index')
    # return render(request,'index.html')
@login_required
def see_favorits(request):
    """See the favorits of the User"""
    user_name = request.user
    print(user_name)
    # if request.user.is_authenticated():
    #     product = UserFavorite.objects.get(user_name=user_name)
    # else:
    #     return render(request,"favorits.html")
    # context = {
    #     'product' : product
    # }
    product = UserFavorite.objects.filter(user_name=user_name)

    
    return render(request,"favorits.html",{'product': product})


