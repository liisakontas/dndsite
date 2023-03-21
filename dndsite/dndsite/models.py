from django.db import models
from django.core.validators import MaxValueValidator

class WildMagicTable(models.Model):
    dice_value = models.IntegerField(validators=[MaxValueValidator(100)])
    effect = models.TextField()
    enabled = models.BooleanField(default=True)
    urls = models.URLField(null=True)