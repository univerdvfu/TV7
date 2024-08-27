from django.db import models

class Sensor(models.Model):
    tv_name = models.CharField(max_length=255, verbose_name='TV Name')
    ip = models.GenericIPAddressField(verbose_name='IP Address')
    port = models.PositiveIntegerField(verbose_name='Port')

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'

    def __str__(self):
        return f"{self.ip}:{self.port}"