from django.urls import path
from pets import views

app_name = "pets"
urlpatterns = [
    path("add/", views.create_pet, name="pet_create"),
    path("", views.list_pet, name="pet_list"),
]
