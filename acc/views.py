from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
#  Create your views here.

def update(request):
    if request.user.is_anonymous:
        return redirect("acc:index")
    if request.method == "POST":
        u = request.user
        um = request.POST.get("umail")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        u.email, u.comment = um, uc
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        return redirect("acc:profile")

    return render(request, "acc/update.html")

def chpass(request):
    if request.user.is_anonymous:
        return redirect("acc:index")
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp,u.password):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect("acc:login")
    return redirect("acc:update")

def signup(request):

    if request.user.is_authenticated:
        return redirect("acc:index")

    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        um = request.POST.get("umail")
        ua = request.POST.get("uage")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, email=um, age=ua, comment=uc, pic=pi)
            return redirect("acc:login")
        except:
            pass
    return render(request, "acc/signup.html")

def delete(request):

    if request.user.is_anonymous:
        return redirect("acc:index")
    
    u = request.user
    cp = request.POST.get("ckpass")
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    return redirect("acc:profile")

def profile(request):
    if request.user.is_anonymous:
        return redirect("acc:index")
    return render(request, "acc/profile.html")

def ulogout(request):
    logout(request)
    return redirect("acc:index")



def index(request):
    context = {
        "d" : {1:"one", 2:"two", 3:"three"}
    }
    return render(request, "acc/index.html", context)




def ulogin(request):

    if request.user.is_authenticated:
        return redirect("acc:index")
    
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            return redirect("acc:index")
        else:
            pass # 메세지
    return render(request, "acc/login.html")