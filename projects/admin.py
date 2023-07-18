from django.contrib import admin
from .models import AdoptMe,Recomendaciones

class AdoptmeAdmin(admin.ModelAdmin):
    readonly_fields=("created",)

class RecomendacionAdmin(admin.ModelAdmin):
    readonly_fields=("created",)
# Register your models here.
admin.site.register(AdoptMe,AdoptmeAdmin)

admin.site.register(Recomendaciones,RecomendacionAdmin)