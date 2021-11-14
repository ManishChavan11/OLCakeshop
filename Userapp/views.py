from django.core.checks import messages
from django.db import models
from django.http.request import HttpRequest
from django.shortcuts import redirect, render,HttpResponse
from Myadmin.models import Categorie,Cake
from .models import UserMaster
from .models import MyCart

# Create your views here.

def home(request):
    cakes=Cake.objects.all()
    categories=Categorie.objects.all()
    return render(request,"master.html",{"categories":categories,"cakes":cakes})

def showcakes(request,id):
    cakes=Cake.objects.filter(category=id)
    categories=Categorie.objects.all()
    return render(request,"master.html",{"categories":categories,"cakes":cakes})

def viewdetails(request,id):
    cakes=Cake.objects.get(category=id)
    categories=Categorie.objects.all()
    return render(request,"Userapp/viewdetails.html",{"categories":categories,"cakes":cakes})

def signup(request):
    if (request.method=="GET"):
        categories=Categorie.objects.all()
        return render(request,"Userapp/signup.html",{"categories":categories})
    else:
        try:
            user = UserMaster.objects.get(username=uname,password=pwd)
        except:    
            uname=request.POST["uname"]
            pwd=request.POST["pwd"]
            #create new object
            u1=UserMaster(uname,pwd)
            #save in database
            u1.save()
            return redirect(home)
        else:
            return HttpResponse("User already exists")

def login(request):
    categories=Categorie.objects.all()
    if ( request.method =="GET"):
        categories = Categorie.objects.all()
        return render(request,"Userapp/login.html",{"categories":categories})
    else:
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        try:
            user = UserMaster.objects.get(username=uname,password=pwd)
            request.session["uname"]=uname
        except:
            message = "Invalid Credentials"
            return render(request,"Userapp/login.html",{"categories":categories,"message":message})
        return redirect(home)

def logout(request):
    #del request.session ["uname"]
    request.session.clear()
    return redirect(home)

def addtocart(request):
    if (request.method=="POST"):
        if "uname" in request.session :
            Categories=Categorie.objects.all()
            c1= MyCart()
            cid = request.POST["cid"]
            cake = Cake.objects.get(id=cid)
            user = UserMaster.objects.get(username=request.session["uname"])
            qty = request.POST["quantity"]
            try:
                m1= MyCart.objects.get(user=user,cake=cake)
            except:
                m1=MyCart()
                m1.user=user
                m1.cake=cake
                m1.qty=qty
                m1.save()
                return redirect(home)
            
        else:
            message= "Please login to add items to cart"
            return redirect(login)
        
def showcartitems(request):
    user = UserMaster.objects.get(username=request.session["uname"])
    cartitems = MyCart.objects.filter(user = user)
    categories = Categorie.objects.all()
    total = 0
    for cart in cartitems:
        total += cart.qty * cart.cake.price

    request.session["total"]= total 
    return render(request,"Userapp/showcartitems.html",{"categories":categories,"cartitems":cartitems})

    
    

def removefromcart(request):
    #categories=Categorie.objects.all()
    if (request.method=="POST") :
        cakeid = request.POST["cakeid"]
        cake = Cake.objects.get(id=cakeid)
        user = UserMaster.objects.get(username = request.session["uname"])
        cartitems = MyCart.objects.get(user=user,cake=cake)
        cartitems.delete()
    return redirect(showcartitems)

def makepayment(request):
    categories=Categorie.objects.all()
    if request.method == "GET":
       return render(request,"Userapp/makepayment.html",{"categories":categories})
    '''else:
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        try:
            user = UserMaster.objects.get(username=uname,password=pwd)
            request.session["uname"]=uname
        except:
            message = "Invalid Credentials"
            return render(request,"Userapp/login.html",{"categories":categories,"message":message})
        return redirect(home)'''

def ev(request):       
    expression=input("Enter your Exp")
    reslt = eval(expression)
    print(reslt)
    
 