from django.urls import path, include

from apps.magistagram.views import registarUsuario

app_name = 'magistagram'
urlpatterns = [
    path('', include([
    #path('', views.ini, name='fhjhj' ),
    path('registro/', registarUsuario, name='registarUsuario' ),
    #path('edadActual/<int:fechaNacimiento>', views.edadActual, name='edadActual')
    ]))
]