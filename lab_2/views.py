from django.shortcuts import render
from .models import Note
from django.http.response import HttpResponse
from django.core import serializers

# Create your views here.
def index(request):
    notes = Note.objects.all()
    response = {'notes': notes}
    return render(request, 'lab2.html', response)

def xml(request):
    data = serializers.serialize('xml', Note.objects.all())
    return HttpResponse(data, content_type="application/xml")

def json(request):
    data = serializers.serialize('json', Note.objects.all())
    return HttpResponse(data, content_type="application/json")