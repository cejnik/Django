from django.contrib import admin
from . models import Film, Screening, Hall, Seat, Reservation

# Register your models here.
admin.site.register(Film)
admin.site.register(Screening)
admin.site.register(Hall)

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display=['hall', 'row', 'number']

