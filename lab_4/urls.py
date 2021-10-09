from django.urls import path
from .views import index, add_note, note_list

urlpatterns = [
    path('', index, name='index_lab4'),
    path('add-note', add_note, name='add_note_lab4'),
    path('note-list', note_list, name='note_list_lab4')
]