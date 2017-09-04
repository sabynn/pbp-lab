from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = ''

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)


# Start of views.py for lab_2_addon

#Create a list of biodata that you wanna show on webpage:
#[{'subject' : 'Name', 'value' : 'Igor'},{{'subject' : 'Birth Date', 'value' : '11 August 1970'},{{'subject' : 'Sex', 'value' : 'Male'}
#TODO Implement
bio_dict = [{'subject' : 'Name', 'value' : mhs_name},{'subject' : 'Birth Date', 'value' : birth_date.strftime('%d %B %Y')},{'subject' : 'Sex', 'value' : ''}]

def index(request):
    response = {}
    return render(request, 'description_lab2addon.html', response)

#End of views.py lab_2_addon