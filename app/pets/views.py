from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from pets.forms import LostPetForm
from pets.models import LostPet
from users.models import User


def create_pet(request):

    # TODO: remover essa gambiarra que foi usada para apresentação
    # o objetivo da gambiarra é permitir a criação de um post sem estar logado
    user = request.user
    if user.is_anonymous:
        user = User.objects.all().first()
    # fim da gambiarra
    form = LostPetForm()
    if request.method == "POST":
        form = LostPetForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = user
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
    pets = LostPet.objects.all()
    context = {"pets": pets}
    return render(request, "pets/pet_list.html", context)
