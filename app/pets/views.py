from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from pets.forms import LostPetForm
from pets.models import PetPost


def create_pet(request):
    form = LostPetForm()
    if request.method == "POST":
        form = LostPetForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            if request.htmx:
                response = HttpResponse()
                response["HX-Location"] = reverse("pets:pet_list")
                return response
            return render(request, "pets/pet_list.html")
        if request.htmx:
            return render(request, "pets/partials/form.html", {"form": form})
    return render(request, "pets/pet_create.html", {"form": form})


def list_pet(request):
    pets = PetPost.objects.all()
    context = {"pets": pets}
    return render(request, "pets/pet_list.html", context)
