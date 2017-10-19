from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class FirstView(TemplateView):
    # template_name = "te"
    def get(self, request, *args, **kwargs):

        return HttpResponse("hello world")