from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    pages = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(500)]
    )

    def __str__(self):
        return f'Název knihy: {self.title} a stránek {self.pages}'

