from django import forms

class PredictForm(forms.Form):

    rainfall = forms.FloatField(label='rainfall', max_length=100)
    radius = forms.FloatField(label='radius', max_length=100)
    elevation = forms.FloatField(label='elevation', max_length=100)
    angle = forms.FloatField(label='angle', max_length=100)
