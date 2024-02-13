from django.shortcuts import render
from django.http import HttpResponse
from blog.models import blog


def Home(request):
    BlogData = blog.objects.all()

    data={
        'BlogData':BlogData
    }
    return render(request,"index.html", data)

def aboutus(request):
    return render(request,"About.html")

def twitter(request):
    return render(request,"Twitter.html")

def header(request):
    return render(request,"header.html")

def Footer(request):
    return render(request,"footer.html")

def privacy(request):
    return render(request,"privacy.html")



