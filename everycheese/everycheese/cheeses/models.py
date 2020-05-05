from django.db import models


from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField

class Cheese(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", 
            unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)


    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "Soft", "soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        HARD = "hard", "Hard"
