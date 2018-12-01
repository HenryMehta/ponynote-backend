from django import forms

from .models import Note

class CreateNoteForm(forms.ModelForm):
  class Meta:
    model = Note
    exclude = ['id', 'owner']