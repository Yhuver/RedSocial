from django.db import models
class Amigo (models.Model):
    
    id= models.AutoField(primary_key=True,)
    fechaAmistad = models.CharField('Titulo', max_length=100, blank=False, null=False, db_column='fechaAmistad')
    seguidor = models.ForeignKey(Usuario,null=False,blank=False,on_delete=models.CASCADE,db_column='seguidor')
    seguido = models.ForeignKey(Usuario, null=False, blank=False,on_delete=models.CASCADE, db_column='seguido')
    
    
    class Meta: #Metaatos del modelo
        verbose_name= 'seguidor' #Que nombre va a recibir el modelo 
        verbose_name_plural = 'segiodores' #Nombre del modelo en plural
        ordering= ["id"] #Para ordenar por un atributo
        db_table = "seguidores"

    def __str__(self):
        return self.imagen

   