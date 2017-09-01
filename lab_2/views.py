from django.shortcuts import render

# Create your views here.

#Create a list of dict that mention all your family member ex:
#[{'status' : 'Father', 'name' : 'Elmo'},{'status' : 'Mother', 'name' : 'Mimo'},{'status' : 'First Son', 'name' : 'Beebah'}
#TODO Implement
family_dict = [{'status' : 'Father', 'name' : 'Asep'},{'status' : 'Mother', 'name' : 'Lia'},{'status' : 'First Son', 'name' : 'Hafiyyan'}]

def index(request):
    response = {'family': family_dict}
    return render(request, 'index_lab2.html', response)