from django.db import models

# Create your models here.
class usuario(models.Model):
    name= models.CharField(max_length=10)
    

class resultados(models.Model):
    puntaje= models.IntegerField()
    usuario= models.ForeignKey(usuario,on_delete=models.CASCADE)#on_Delete sirve para eliminar los datos
                                                                #de la tabla