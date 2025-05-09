from django import forms
from pets.models import PetPost


class LostPetForm(forms.ModelForm):
    class Meta:
        model = PetPost
        exclude = (
            "created_by",
            "owner",
        )
