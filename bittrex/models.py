from django.db import models


class BTCSummary(models.Model):
    symbol = models.CharField(max_length=20)
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()
    quote_volume = models.FloatField()
    percent_change = models.FloatField()
    updated_at = models.DateTimeField()
