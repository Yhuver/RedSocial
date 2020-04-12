from django.shortcuts import render

# Create your views here.

def registarUsuario(request):
    return render(request,'registrar.html')
