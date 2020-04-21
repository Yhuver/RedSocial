from django.db import models



class Publicacion (models.Model):
    id= models.AutoField(primary_key=True,)
    imagen = models.CharField('Titulo', max_length=100, blank=False, null=False, db_column='imagen')
    fechaPublicacion = models.CharField('Titulo', max_length=100, blank=False, null=False, db_column='fechaPublicacion')
    usuario_id = models.ForeignKey(Usuario,null=False,blank=True,on_delete=models.CASCADE)
    comentario = models.CharField('Titulo', max_length=255, blank=False, null=False, db_column='comentario')
    
    
    class Meta: #Metaatos del modelo
        verbose_name= 'Publicacion' #Que nombre va a recibir el modelo 
        verbose_name_plural = 'Publicaciones' #Nombre del modelo en plural
        ordering= ["id"] #Para ordenar por un atributo
        db_table = "publicacion"

    def __str__(self):
        return self.imagen

    def setName(self, imagen):
        self.imagen=imagen
        