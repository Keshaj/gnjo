from django.contrib import admin

from .models import Room, AttendEvent, Event

# Register your models here.
admin.site.register(Room)
admin.site.register(Event)
admin.site.register(AttendEvent)
