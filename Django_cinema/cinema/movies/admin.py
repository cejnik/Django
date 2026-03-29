from django.contrib import admin
from . models import Film, Screening, Hall

# Register your models here.
admin.site.register(Film)
admin.site.register(Screening)
admin.site.register(Hall)
