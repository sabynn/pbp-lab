import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from lab_2.models import Note
from lab_4.forms import NoteForm


def index(request):
    notes = Note.objects.all()
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

    response = {'notes': notes}
    response['form'] = form
    return render(request, 'lab5_index.html', response)


def view_note(request, id):
    obj = Note.objects.get(id=id)
    data = serializers.serialize('json', [obj, ])

    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type='application/json')
