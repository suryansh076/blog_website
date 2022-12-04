from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class Blogform(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=['content']


#   content = forms.CharField(widget=FroalaEditor)