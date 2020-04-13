from django.shortcuts import render
from apps.magistagram.models.usuario import Usuario

# Create your views here.

def enviarFormregistarUsuario(request):
    return render(request,'registrar.html')

def registrarUsuario(request):
    message=None
    if request.method == "POST":
        print('Aquí')
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('username'))
        print(request.POST.get('pass'))
        print('---------------------------------------------------')
        usser=Usuario(nombre=request.POST.get('name'),email=request.POST.get('email'),
        Usuario=request.POST.get('username'),clave=request.POST.get('pass'),)
        usser.save()
        message={'message': 'Registro exitoso'}

    print('---------------------------------------------------')
    print('Lista de usuarios')
    lista = Usuario.objects.all() 
    print(lista)
    print('---------------------------------------------------')
    print('***************************************************')
    print('---------------------------------------------------')
    print('Buscar usuario especifico')
    lista = Usuario.objects.get(pk=1)
    print(lista.email)
    print('---------------------------------------------------')
    print('***************************************************')
    print('---------------------------------------------------')
    print('Actualizar usuario especifico')
    var = Usuario.objects.get(pk=2)
    var.nombre="mita"
    var.save()
    print('---------------------------------------------------')
    print('***************************************************')
    print('---------------------------------------------------')
    print('eliminar usuario especifico')
    var = Usuario.objects.get(pk=2)
    var.delete()
    print('---------------------------------------------------')
    return render(request, 'login.html', message)
