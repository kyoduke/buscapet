from django.db import models
from django.utils.translation import gettext_lazy as _


class LostPet(models.Model):
    class PetSpecies(models.IntegerChoices):
        OTHER = 0, _("Other")
        DOG = 1, _("Dog")
        CAT = 2, _("Cat")
        BIRD = 3, _("Bird")

    class PetGender(models.IntegerChoices):
        UNKNOWN = 0, _("Unknown")
        MALE = 1, _("Male")
        FEMALE = 2, _("Female")

    class PetStatus(models.IntegerChoices):
        LOST = 0, _("Lost")
        FOUND = 1, _("Found")

    status = models.SmallIntegerField(choices=PetStatus, default=PetStatus.LOST, verbose_name=_("register"))

    name = models.CharField(max_length=100, null=True, default=_("Unknown"), verbose_name=_("name"))
    owner = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="pets", null=True, verbose_name=_("owner")
    )
    species = models.SmallIntegerField(choices=PetSpecies, default=PetSpecies.OTHER, verbose_name=_("species"))
    predominant_color = models.CharField(max_length=50, null=True, verbose_name=_("predominant color"))
    gender = models.SmallIntegerField(choices=PetGender, default=PetGender.UNKNOWN, verbose_name=_("gender"))

    description = models.TextField(null=True, verbose_name=_("description"))

    address = models.CharField(max_length=255, verbose_name=_("address"))
    state = models.CharField(max_length=64, verbose_name=_("state"))
    city = models.CharField(max_length=128, verbose_name=_("city"))

    created_by = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="created_pets"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)


# TODO: Community Found Feedback system. An input with "Has this pet been found?" and a thumbs up or down.

# TODO: Rating system so the community can rate relevant posts. Is this a good idea? Probably not, we don't want a social media kinda of feeling.
