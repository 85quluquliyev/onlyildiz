from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, "viewTemplates/homepage.html")


def aboutPage(request):
    return render(request, "viewTemplates/about.html")