from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AdoptMe(models.Model):
    Nombre=models.CharField(max_length=50,blank=False)
    Imagen=models.ImageField(upload_to="productos/",null=True,blank=False)
    Raza=models.CharField(max_length=100,blank=False)
    sexo=models.CharField(max_length=10,blank=False) 
    Descripcion=models.TextField(blank=False,max_length=250)
    RedSocial=models.CharField(max_length=20,blank=False,null=True)
    datecompleted=models.DateTimeField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.Nombre +' - ' + self.Raza +' -by ' + self.user.username
    
    class Meta:
        ordering=["-created"]
    
class Recomendaciones(models.Model):
    titulo=models.CharField(max_length=50,blank=False,null=False)
    mensaje=models.TextField(max_length=400,blank=False,null=False)
    created=models.DateTimeField(auto_now_add=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return 'by: ' + self.user.username
    
    class Meta:
        ordering=["-created"]
    