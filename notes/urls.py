from django.urls import path
from . import views

urlpatterns = [
  path('', views.NoteList.as_view(), name="home"),
  path('create-note', views.CreateNote.as_view(), name="create-note"),
  path('delete-note/<int:pk>/', views.DeleteNote.as_view(), name="delete-note")
  
]