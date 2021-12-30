from django.forms import forms

class ImageUpload(forms.Form):
    image= forms.ImageField(label='Select a file', )
    number = forms.CharField()