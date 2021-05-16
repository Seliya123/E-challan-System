from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import challans
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.
def index(request):
    context = {
         'posts' : Post.objects.all()  
     }
    return render(request, "index.html", context)
   
def finedetails(request):
    return render(request, "finedetails.html")

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
       
        if user is not None:
            login(request,user)
            return redirect('/challan')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}

    return render(request, "login.html", context)

def logouts(request):
    logout(request)
    
    return redirect('/')

@login_required(login_url='/logins')
def challan(request):

     if request.method == "POST":
        # challans = challan()
        names = request.POST.get('names')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')
        licensenumber = request.POST.get('licensenumber')
        vehiclenumber = request.POST.get('vehiclenumber')
        vehicletype = request.POST.get('vehicletype')
        creator = request.POST.get('creator')

        ins = models.challans(names = names, phonenumber = phonenumber,  address = address, licensenumber = licensenumber, vehiclenumber=vehiclenumber, vehicletype=vehicletype, creator=creator)
        ins.save()

    
     return render(request, "challan.html")

@login_required(login_url='/logins')
def records(request):

    rec = challans.objects.filter(creator = request.user)

    return render(request, "records.html", {"record" : rec })



    