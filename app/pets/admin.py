from django.contrib import admin

from .models import PetPost


@admin.register(PetPost)
class PetAdmin(admin.ModelAdmin):
    pass
