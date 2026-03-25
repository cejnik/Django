from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']