from tkinter import Widget
from turtle import width
from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'subject', 'standard', 'unit', 'pdf')
        c = 'col-md-6 form-control'
        s = ''
        widgets = {
            'title': forms.TextInput(attrs={'class': c, 'style': s, 'placeholder': 'eg:classNotes,QB'}),
            'subject': forms.Select(attrs={'class': c, 'style': s}),
            'standard': forms.Select(attrs={'class': c, 'style': s}),
            'unit': forms.Select(attrs={'class': c, 'style': s}),
            'pdf': forms.FileInput(attrs={'class': c, 'style': s})
        }
