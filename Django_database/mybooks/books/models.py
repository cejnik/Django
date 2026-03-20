from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    pages = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(500)]
    )
    author = models.CharField(null=True,max_length=50)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f'Název knihy: {self.title} s autorem: {self.author} a stránek {self.pages}, a je to bestseller: {self.is_bestseller}'

