from django.shortcuts import render
from .models import Product,Category,UserFavorite
import requests
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home_function(request):
    # all_entries = Entry.objects.filter(name="Julien")
    # print(all_entries)
    return render(request,"index.html")

def searchresult(request):
    query = request.GET.get('query')
    if not query:
        product = Product.objects.all
    else:
        product = Product.objects.filter(name__contains=query)
    name = "Résultats pour la requête %s"%query
    # title = 'Votre recherche est :  "{}"'. format(query)
    # context = {
    #     'name': name
    #     # 'data': data
    #     }
    # product = Product.objects.filter(name__contains=query)
    # product = Product.objects.all()[5]
    print(product)
    # return render(request,"search_result.html",context)
    return render(request,"search_result.html",{'product': product})
