from django import forms
from .models import Song

class SongForm(forms.ModelForm):

    title = forms.CharField(max_length=100)
    file = forms.FileField()

    class Meta:
        model = Song
        fields = ['title', 'file']
