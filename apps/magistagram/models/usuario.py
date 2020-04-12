from django.db import models

class usuario(models.Model):
    id= models.AutoField(primary_key=True,)
    nombre = models.CharField('Titulo', max_length=50, blank=False, null=False, db_column='nombre')
    email = models.CharField('Titulo', max_length=100, blank=False, null=False, db_column='email')
    usuario = models.CharField('Titulo', max_length=50, blank=False, null=False, db_column='usuario')
    clave = models.CharField('Titulo', max_length=255, blank=False, null=False, db_column='password')
    # autor_id=models.OneToOneField(Autor, on_delete=models.CASCADE) crea una llave foranea en Libro 
    # de la relación uno a uno
    
    # autor_id=models.ForeignKey(Autor, on_delete=models.CASCADE) crea una llave foranea en Libro
    # de relacion uno a muchos, la parte que contiene el muchos es la clase acual

    #autor_id=models.ManyToManyField(Autor)Crea una tabla intermedia entre libro y Autor


    class Meta: #Metaatos del modelo
        verbose_name= 'Libro' #Que nombre va a recibir el modelo 
        verbose_name_plural = 'Libros' #Nombre del modelo en plural
        ordering= ["nombre"] #Para ordenar por un atributo
        db_table = "usuarios"

    def __str__(self):
        return self.nombre