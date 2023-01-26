from django.db import models
from django.utils import timezone

# Create your models here.
class Weather(models.Model):
    location = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            self.date = timezone.now()
        return super(Weather, self).save(*args, **kwargs)
