from django.urls import path, include

from apps.magistagram.views import registrarUsuario, enviarFormregistarUsuario

app_name = 'magistagram'
urlpatterns = [
    path('', include([
    #path('', views.ini, name='fhjhj' ),
    path('registro/', enviarFormregistarUsuario, name='formularioRegistro' ),
    path('registrarUsuario/', registrarUsuario, name='registroUsuario' ),
    #path('edadActual/<int:fechaNacimiento>', views.edadActual, name='edadActual')
    ]))
]