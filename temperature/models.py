from django.db import models

# Create your models here.

class TemperatureReading(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Temperature reading at {self.timestamp}: {self.value}"
