from django.http import HttpResponseRedirect
from django.shortcuts import render
from lab_2.models import Note
from lab_4.forms import NoteForm


# Create your views here.
def index(request):
    notes = Note.objects.all()
    response = {'notes': notes}
    return render(request, 'lab4_index.html', response)


def add_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/lab-4")
    response = {'form': form}
    return render(request, 'lab4_form.html', response)


def note_list(request):
    notes = Note.objects.all()
    response = {'notes': notes}
    return render(request, 'lab4_note_list.html', response)
