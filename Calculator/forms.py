from django import forms

class Calc(forms.Form):
    num1 = forms.IntegerField(required=True)
    num2 = forms.IntegerField(required=True)