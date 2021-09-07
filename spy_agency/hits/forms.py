from django import forms
from django.db.models.fields import CharField
from .utils import functions

from django.forms import ModelForm
from .models import Hit

class HitForm(ModelForm):    

    class Meta:
        model = Hit
        fields = ['hitman', 'description', 'target']

    def __init__(self,*args,**kwargs):
        user = kwargs.pop("user")
        super(HitForm, self).__init__(*args,**kwargs)
        self.fields['hitman'] = forms.ModelChoiceField(label="Hitman", queryset=functions.get_hitmen(user), widget=forms.Select)
