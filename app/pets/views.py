from django.shortcuts import render
from pets.forms import LostPetForm


def create_pet(request):
    form = LostPetForm()
    if request.method == "POST":
        form = LostPetForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return render(request, "pets/pet_list.html")
    return render(request, "pets/pet_create.html", {"form": form})
