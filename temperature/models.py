from django.db import models

# Create your models here.

class TemperatureReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    def __str__(self):
        return f"Temperature reading at {self.timestamp}: {self.value}"
