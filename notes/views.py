from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView

from .forms import CreateNoteForm
from .models import Note
# Create your views here.

class NoteList(ListView):
  model = Note

class CreateNote(CreateView):
  model = Note
  form_class = CreateNoteForm
  success_url = '/'

class DeleteNote(DeleteView):
  model = Note
  success_url = '/'