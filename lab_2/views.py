from django.shortcuts import render
from lab_1.views import mhs_name
# Create your views here.

#Create a content paragraph for your landing page:
#TODO Implement
landing_page_content = 'I try yo create simple and elegant websites.\
 This is just the beginning of my long journey to create a simple website while enrolling at\
  Web Programming and Designing Course in Faculty of Computer Science Universitas Indonesia.'


def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)