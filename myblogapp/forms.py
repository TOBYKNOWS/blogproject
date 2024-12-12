from django import forms

class FormInput(forms.Form):
    firstname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    address = forms.CharField(max_length=50)


    