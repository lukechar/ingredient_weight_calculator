from django.db import models
from django import forms

# Ingredients
INGREDIENTS = (
    (None, 'Select Ingredient'),
    (528.34, 'All-Purpose Flour'),
    (536.80, 'Bread Flour'),
    (536.80, '00 Flour'),
    (547.78, 'Whole Wheat Flour'),
    (431.13, 'Rye Flour'),
    (515.66, 'Gluten-Free Flour'),
    (507.21, 'Buckwheat Flour'),
    (515.66, 'Tapioca Flour'),
    (473.40, 'Coconut Flour'),
    (1029.05, 'Baking Powder'),
    (2200.00, 'Baking Soda'),
    (1000.0, 'Water'),
)

# Volume units
VOLUME_UNITS = (
    (0.236588, 'Cups'),
    (0.946353, 'Quarts'),
    (3.78541, 'Gallons'),
    (0.0295735, 'Fluid Ounces'),
    (0.0147868, 'Tablespoons'),
    (0.00492892, 'Teaspoons'),
    (0.001, 'Milliliters'),
    (1.0, 'Liters'),
)

class IngredientCalcForm(forms.Form):
    ingredient = forms.ChoiceField(choices=INGREDIENTS, required=True)
    volume = forms.DecimalField(
        label='Volume',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Volume'})
    )
    volume_units = forms.ChoiceField(choices=VOLUME_UNITS)