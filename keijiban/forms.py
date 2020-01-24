from django import forms

class KakikomiForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField()


class GeoTimeForm(forms.Form):
    start = forms.CharField(
                label='start',
                max_length=50,
                required=True,
                widget=forms.TextInput()
            )
    goal  = forms.CharField(
                label='goal',
                max_length=50,
                required=True,
                widget=forms.TextInput()
            )
