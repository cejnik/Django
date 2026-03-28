from django.db import models
from django.utils.text import slugify

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    duration = models.PositiveSmallIntegerField()
    release_year = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
    
    #Logic to Slugify
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Screening(models.Model):
    film = models.ForeignKey(Film , on_delete=models.CASCADE )
    screening_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
