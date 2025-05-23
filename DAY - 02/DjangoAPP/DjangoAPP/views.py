from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render 


# def demo(request):
#     return HttpResponse("<h1>Welcome to <i>Django</i></h1>")


#urlRoute = '''<h2>Click on the link below to redirect</h2><a href='/'>Home Page</a><br><br><a href='/about/'>About Page</a><br><br><a href='/contact/'>Contacts</a><br><br><a href='/service/'>Services</a><br><br><a href='/register/'>Register Page</a><br><br><a href='/login/'>Login Page</a><br><br>'''

# def home(request):
#     return HttpResponse("<h1>Home Page</h1>"+urlRoute)

# def home(request):
#     return render(request,"home.html")

# def about(request):
#     return HttpResponse("<h1>About Page</h1>"+urlRoute)

# def contact(request):
#     return HttpResponse("<h1>Contact Page</h1>"+urlRoute)

# @csrf_exempt
# def service(request):
#     if request.method=='GET':
#         new_msg = "<h2>Service Page with GET Method</h2>"
#     elif request.method=='POST':
#         new_msg = "<h2>Service Page with POST Method</h2>"
#     elif request.method=='PUT':
#         new_msg = "<h2>Service Page with PUT Method</h2>"
#     elif request.method=='PATCH':
#         new_msg = "<h2>Service Page with PATCH Method</h2>"
#     elif request.method=='DELETE':
#         new_msg = "<h2>Service Page with DELETE Method</h2>"
#     else : 
#         new_msg = "<h2>Service Page with Another Method</h2>"
    
#     return HttpResponse(new_msg+urlRoute)

# def register(request):
#     return HttpResponse("<h1>Register Page</h1>"+urlRoute)

# def login(request):
#     return HttpResponse("<h1>Login Page</h1>"+urlRoute)




def home(request):
    return render(request,"home.html")

def about(request):
    a,b = 200 , 100
    c=a+b

    mks = [12,34,56,78]

    empDetails = {"eno":1001,"enm":"Vivek","esal":1000000}

    return render(request,"about.html",{"a":a,"b":b,"c":c,"marks":mks,"empDetails":empDetails})

def contact(request):
    users = [{"uid":1001,"unm":"@username1","upass":"xyz@123"},
             {"uid":1002,"unm":"@username2","upass":"xyz@321"},
             {"uid":1003,"unm":"@username3","upass":"xyz@000"}]

    return render(request,"contact.html",{"users":users})

def service(request):   
    return render(request,"service.html")

def register(request):
    if request.method=="GET":
        return render(request,"register.html")
    else :
        print(request.POST)
        return render(request,"register.html")

    
def login(request):
    return render(request,"login.html")