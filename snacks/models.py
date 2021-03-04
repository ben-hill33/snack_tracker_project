from django.db import models
from datetime import datetime, timezone


class Snacks(models.Model):
    snack_name = models.CharField(max_length=64)
    description = models.TextField()
    purchaser = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name

    def timestamp(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
