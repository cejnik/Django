from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Název filmu')
    length = models.IntegerField(validators=[MinValueValidator(45), MaxValueValidator(200)], default=90, verbose_name='Délka v minutách')
    is_for_adults = models.BooleanField(default=False, verbose_name='Pouze pro dospělé')
    description = models.TextField(blank=True, null=True, verbose_name='Popis')
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name='Hodnocení'
    )

    def __str__(self):
        return f'{self.title} ({self.length} min)'



