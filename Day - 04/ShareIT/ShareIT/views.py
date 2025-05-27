from django.http import HttpResponse
from django.shortcuts import render , redirect

from . import models 
import time

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")

def login(request):
    if request.method=="GET":    
        return render(request,"login.html",{"output":""})
    else:
        #to recieve data from UI 'form'
        email=request.POST.get("email")
        password=request.POST.get("password")

        #to check record in database
        userDetails=models.Register.objects.filter(email=email,password=password,status=1)

        if len(userDetails)>0:
            if(userDetails[0].role=="admin"):
                return redirect("/myadmin/")
            else :
                return redirect("/user/")
        else:
            return render(request,"login.html",{"output":"Invalid user or verify your account...."})


def register(request):
    if request.method=="GET":
        return render(request,"register.html",{"output":""})
    else:
        #to recieve data from UI 'form'
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        city=request.POST.get("city")
        gender=request.POST.get("gender")

        #to insert record in database using models
        p=models.Register(name=name,email=email,password=password,mobile=mobile,address=address,city=city,gender=gender,status=0,role="user",info=time.asctime())
        p.save()
        return render(request,"register.html",{"output":"User register successfully...."})
    
def adminhome(request):
    return render(request,"adminhome.html")

def userhome(request):
    return render(request,"userhome.html")

def manageusers(request):

    userDetails = models.Register.objects.filter(role="user")
    print(userDetails)
    return render(request,"manageusers.html",{"userDetails" : userDetails})

def manageuserstatus(request):
    
    s = request.GET.get("s")
    regid = int (request.GET.get("regid"))

    if s=="active" : 
        models.Register.objects.filter(regid=regid).update(status=1)
    elif s=="inactive" : 
        models.Register.objects.filter(regid=regid).update(status=0)
    else :
        models.Register.objects.filter(regid=regid).delete()

    return redirect("/manageusers/")