from django.db import models
from datetime import datetime, timezone
from django.urls import reverse
from django.contrib.auth import get_user_model


class Snacks(models.Model):
    snack_name = models.CharField(max_length=64, help_text="Enter a SNACK!")
    description = models.TextField()
    snack_amount = models.IntegerField(default=10)
    purchaser = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.snack_name

    def timestamp(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
