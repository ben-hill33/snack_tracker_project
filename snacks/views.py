from django.shortcuts import render
from snacks.models import Snacks
from django.views.generic import TemplateView


class SnacksView(TemplateView):
    template_name = "snacks.html"
    model = Snacks


# gonna need that
# class SnackDetailView(SnacksView):
