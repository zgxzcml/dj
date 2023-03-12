from django.shortcuts import render, redirect
from .models import Topic, Choice
# Create your views here.
def index(request):
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(request, "vote/index.html", context)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(request, "vote/detail.html", context)

def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        t = Topic(subject=s, maker=request.user, content=c)
        t.save()
        cn = request.POST.getlist("cname")
        cc = request.POST.getlist("ccomm")
        for n, c in zip(cn,cc):
            Choice(name=n, comment=c, top=t).save()
        return redirect("vote:index")
    return render(request, "vote/create.html")

def cancel(request, tpk):
    u = request.user
    t = Topic.objects.get(id=tpk)
    t.voter.remove(u)
    u.choice_set.get(top=t).choicer.remove(u)
    return redirect("vote:detail", tpk)

def delete(request, tpk):
    t = Topic.objects.get(id=tpk)
    if request.user == t.maker:
        t.delete()
    return redirect("vote:index")



def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect("vote:detail", tpk)