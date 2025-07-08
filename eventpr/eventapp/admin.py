from django.contrib import admin
from .models import Event,Booking
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'combo_offer_price']

admin.site.register(Event, EventAdmin)
admin.site.register(Booking)