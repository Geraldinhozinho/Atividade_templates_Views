from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'My_app/Home.html')

def Portifolio(request):
    return render(request, 'My_app/Portifolio.html')