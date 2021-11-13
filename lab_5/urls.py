from django.urls import path
from .views import index, view_note

urlpatterns = [
    path('', index, name='index_lab5'),
    path('notes/<int:id>', view_note, name="view_note"),
    # path('notes/<int:id>/update', update_note, name="update_notes"),
    # path('notes/<int:id>/delete', delete_note, name="delete_notes"),

]