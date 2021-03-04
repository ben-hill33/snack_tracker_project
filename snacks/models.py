from django.db import models
from datetime import datetime, timezone
from django.urls import reverse


class Snacks(models.Model):
    snack_name = models.CharField(max_length=64, help_text="Enter a SNACK!")
    description = models.TextField()
    purchaser = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.snack_name

    def timestamp(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # once view and template are set up for this, try this sumbitch
    # def get_absolute_url(self):
    #     return reverse("snack_detail", args=[str(self.id)])
