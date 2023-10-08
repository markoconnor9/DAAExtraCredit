from django import forms


from .models import *

class selectForm(forms.Form):
    day = forms.ModelChoiceField(queryset=(Employee.objects.values_list('name',flat=True)))
