from django.urls import path, include
from django.contrib.auth import  login, logout
from apps.magistagram.views import registrarUsuario
from apps.magistagram.views import enviarFormlogin,enviarFormpublicacion,enviarFormregistarUsuario

app_name = 'magistagram'
urlpatterns = [
    path('', include([
    #path('', views.ini, name='fhjhj' ),
    path('registro/', enviarFormregistarUsuario, name='formularioRegistro' ),
    path('registrarUsuario/', registrarUsuario, name='registroUsuario' ),
    #path('login/',enviarFormlogin,name='loginUsuario' ),
    #path('logeo/',login,name='logeonUsuario' ),
    path('publicacion/',enviarFormpublicacion,name='publicar'),
    path('login/',login,{'Template_name':'PaginaPrincipal.html'},name='login'),
    #path('edadActual/<int:fechaNacimiento>', views.edadActual, name='edadActual')
    ]))
]