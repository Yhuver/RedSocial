from django.shortcuts import render
from django.contrib.auth import authenticate
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
        usuario=request.POST.get('username'),clave=request.POST.get('pass'))
        usser.save()
        message={'message': 'Registro exitoso'}
        return render(request, 'login.html', message)
    
        
        
def actualizarUsuario(request):
    
    print('Actualizar usuario especifico')
    var =Usuario.objects.get(pk=2)
    var.nombre="mita"
    var.save()
    
    
def eliminarUsuario(request):
    print('eliminar usuario especifico')
    var = Usuario.objects.get(pk=2)
    var.delete()
    
def listarUsuarios(request):
    
    print('Lista de usuarios')
    lista = Usuario.objects.all() 
    print(lista)
    
#-------------login de usuarios----------

def enviarFormlogin(request):
    return render(request,'login.html')


def login(request):
    usu=(request.POST.get('username'))
    passw=(request.POST.get('password'))
    message=None
    if request.method=='POST':
        usuario=Usuario.objects.get(usuario=usu)

        if usuario.clave==passw:
            message={'message': 'BienVenido'+usuario.nombre}
            
            return render(request,'PaginaPrincipal.html',message)
        
    return render(request,'login.html')

#-----------------publicar------------------------
def enviarFormpublicacion(request):
    return render(request,'publicacion.html')



def publicar (request):
    imagen=
    fechaPublicacion=
    usuarios_id=
    comentario=
    

    
#-----------------seguir usuario------------------

#def seguir (request):
 #   FA=datetime.now()
  #  fechaAmistad=str(FA)
    
        
        
    
    
        
        