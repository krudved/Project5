from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"online.html")


def showdetails(request):
    na = request.POST.get("t1")
    age = request.POST.get("t2")
    email = request.POST.get("t3")
    uname = request.POST.get("t4")
    d = {"name":na,'age':age,'email':email,'uname':uname}
    return render(request,"online.html",{'data':d})