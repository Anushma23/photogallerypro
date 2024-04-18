from django import forms

from app1.models import Photo


class Gallery(forms.ModelForm):
    class Meta:
        model=Photo
        fields='__all__'