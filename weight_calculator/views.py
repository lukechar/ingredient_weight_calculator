from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the Ingredient Weight Calculator index.")