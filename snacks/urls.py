from django.urls import path
from .views import SnacksView

urlpatterns = [
    path("", SnacksView.as_view(), name="snacks"),
    # need a primary key path here, obviously, you dolt. That's rubbish!
]
