from django import forms
from todoapp.models import Articles

class postform(forms.ModelForm):
    class Meta():
        model = Articles
        fields = '__all__'
    