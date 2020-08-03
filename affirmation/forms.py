from django import forms
from .models import Affirmation

class AffirmationForm(forms.Form):
     class Meta:
        model = Affirmation
        # fields = ['name']
 
   