from django import forms
from pets.models import LostPet


class LostPetForm(forms.ModelForm):
    class Meta:
        model = LostPet
        exclude = (
            "created_by",
            "owner",
        )

