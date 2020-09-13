from django.shortcuts import render
from .models import *
import requests

# Create your views here.
def home_function(request):
    # all_entries = Entry.objects.filter(name="Julien")
    # print(all_entries)
    return render(request,"index.html")