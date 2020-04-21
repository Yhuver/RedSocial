from django.db import models


class Comentario (models.Model):
    idComentario= models.AutoField(primary_key=True,)
    fechaComentario = models.CharField('Titulo', max_length=100, blank=False, null=False, db_column='fechaComentario')
    mensaje = models.CharField('Titulo', max_length=200, blank=False, null=False, db_column='mensaje')
    usuario_id = models.ForeignKey(Usuario,null=False,blank=False,on_delete=models.CASCADE,db_column='usuarios_id')
    publicacion_id = models.ForeignKey(Publicacion, null=False,blank=False, on_delete=models.CASCADE,db_column='publicacion_id')
    
    
    class Meta: #Metaatos del modelo
        verbose_name= 'Comentario' #Que nombre va a recibir el modelo 
        verbose_name_plural = 'Comentarios' #Nombre del modelo en plural
        ordering= ["idComentario"] #Para ordenar por un atributo
        db_table = "comentarios"

    def __str__(self):
        return self.imagen

    def setName(self, imagen):
        self.imagen=imagen