from django.contrib import admin
from .models import (
    Sensor,
)

@admin.register(Sensor)
class TVSensor(admin.ModelAdmin):
    list_display = ('id', 'tv_name', 'ip', 'port')

admin.site.unregister(Sensor)
admin.site.register(Sensor, TVSensor)