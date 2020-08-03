from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import IngredientCalcForm


OUNCES_IN_GRAM = 0.035274
LBS_IN_GRAM = 0.00220462442

def calculator_form(request):
    form = IngredientCalcForm()
    return render(request, 'weight_calculator/calculator.html', {'form': form, 'title': 'Ingredient Weight Calculator'})

def calculate(request):
    if not request.GET.get('volume', None) or not request.GET.get('volume_units', None) or not request.GET.get('ingredient', None):
        return JsonResponse({'result': False})
    volume = float(request.GET.get('volume', None))
    volume_units = float(request.GET.get('volume_units', None))
    ingredient = float(request.GET.get('ingredient', None))
    weight_grams = volume * volume_units * ingredient
    weight_kg = volume * volume_units * ingredient / 1000
    weight_oz = weight_grams * OUNCES_IN_GRAM
    weight_lbs = weight_grams * LBS_IN_GRAM
    data = {
        'result': True,
        'provided_volume': "{:.2f}".format(volume),
        'provided_volume_units': volume_units,
        'provided_ingredient': ingredient,
        'weight_grams': "{:.2f}".format(weight_grams),
        'weight_kg': "{:.2f}".format(weight_kg),
        'weight_oz': "{:.2f}".format(weight_oz),
        'weight_lbs': "{:.2f}".format(weight_lbs),
    }
    return JsonResponse(data)
    