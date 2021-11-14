from django.contrib import admin
from .models import Categorie,Cake

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=["catname"]

class CakeAdmin(admin.ModelAdmin):
    list_display=["cakename","price","description","category"]
    

admin.site.register(Categorie,CategoryAdmin)
admin.site.register(Cake,CakeAdmin)