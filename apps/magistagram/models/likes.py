from django.db import models


class Like (models.Model):
    id= models.AutoField(primary_key=True,)
    fecha = models.CharField('Titulo', max_length=100, blank=False, null=False, db_column='fecha')
    usuario_id = models.ForeignKey(Usuario,null=False,blank=False,on_delete=models.CASCADE,db_column='usuarios_id')
    publicacion_id = models.ForeignKey(Publicacion, null=False,blank=False, on_delete=models.CASCADE,db_column='publicacion_id')
    
    
    class Meta: #Metaatos del modelo
        verbose_name= 'like' #Que nombre va a recibir el modelo 
        verbose_name_plural = 'liks' #Nombre del modelo en plural
        ordering= ["id"] #Para ordenar por un atributo
        db_table = "likes"

    def __str__(self):
        return self.mensaje

   