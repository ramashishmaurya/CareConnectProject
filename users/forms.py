from django import forms
from .models import tweets

class tweetsform(forms.ModelForm):
    class meta:
        model = tweets
        fields =['text','photo']