from django import forms
from .models import AdoptMe,Recomendaciones
from django.forms import ModelForm

MACHO=0
HEMBRA=1
opciones_genero=(
    (MACHO,'Macho'),
    (HEMBRA,'Hembra')
)

class CreatePostForm(forms.ModelForm):
    class Meta:
        model=AdoptMe
        fields=['Nombre','Imagen','Raza','sexo','Descripcion','RedSocial']
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de la mascota'}),
            'Imagen':forms.FileInput(attrs={'class':'form-control'}),
            'Raza':forms.TextInput(attrs={'class':'form-control','placeholder':'Raza de la mascota'}),
            'sexo':forms.TextInput(attrs={'class':'form-control','placeholder':'Macho/Hembra'}),
            'Descripcion':forms.Textarea(attrs={'class':'form-control','placeholder':'Añade una descripción'}),
            'RedSocial':forms.TextInput(attrs={'class':'form-control','placeholder':    '+51/Instagram'})
        }

class CrearRecomendacion(forms.ModelForm):
    class Meta:
        model=Recomendaciones
        fields=['titulo','mensaje']
        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
            'mensaje':forms.TextInput(attrs={'class':'form-control','placeholder':'Añada su recomendación'})
        }