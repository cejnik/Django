from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=50, verbose_name='Název písničky')
    length = models.FloatField(verbose_name='Délka v min')
    author = models.CharField(max_length=50, verbose_name='Autor')
    description = models.CharField(max_length=50, verbose_name='Popis')
    rating = models.FloatField(verbose_name='Rating')
    is_popular = models.BooleanField(verbose_name='Je populární?')
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])
        