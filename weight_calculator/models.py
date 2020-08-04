from django.db import models
from django import forms

# Ingredients with g/L values
INGREDIENTS = (
    ('Flour', (
        (528.34, 'All-Purpose Flour'),
        (536.80, 'Bread Flour'),
        (536.80, '00 Flour'),
        (547.78, 'Whole Wheat Flour'),
        (431.13, 'Rye Flour'),
        (515.66, 'Gluten-Free Flour'),
        (507.21, 'Buckwheat Flour'),
        (515.66, 'Tapioca Flour'),
        (473.40, 'Coconut Flour'),
        )
    ),
    ('Liquids', (
        (997.00, 'Water, tap'),
        (998.20, 'Water, distilled'),
        (1030.00, 'Milk'),
        (1036.00, 'Buttermilk'),
        (880.00, 'Vanilla extract, natural'),
        (879.00, 'Vanilla extract, imitation'),
        (940.00, 'Rum'),
        (960.00, 'White Vinegar')
        )
    ),
    ('Leavening Agents', (
        (1029.05, 'Baking Powder'),
        (2200.00, 'Baking Soda'),
        )
    ),
    ('Other Dry Ingredients', (
        (836.90, 'Sugar, white'),
        (801.00, 'Sugar, powdered'),
        (430.00, 'Cocca Powder'),
        (845.35, 'Sugar, brown'),
        (528.33, 'Cornstarch'),
        (449.00, 'Milk, powdered'),
        )
    ),

)

# Volume units (in liters)
VOLUME_UNITS = (
    ('US', (
        (0.236588, 'Cups'),
        (0.946353, 'Quarts'),
        (3.78541, 'Gallons'),
        (0.0295735, 'Fluid Ounces'),
        (0.0147868, 'Tablespoons'),
        (0.00492892, 'Teaspoons'),
        )
    ),
    ('Metric', (
        (0.001, 'Milliliters'),
        (1.0, 'Liters'),
    )
    ),
)

class IngredientCalcForm(forms.Form):
    ingredient = forms.ChoiceField(choices=INGREDIENTS, required=True)
    volume = forms.DecimalField(
        label='Volume',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Volume'})
    )
    volume_units = forms.ChoiceField(choices=VOLUME_UNITS)