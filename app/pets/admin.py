from django.contrib import admin

from .models import LostPet


@admin.register(LostPet)
class PetAdmin(admin.ModelAdmin):
    pass