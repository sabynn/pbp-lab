from django.shortcuts import render

# Create your views here.

#Create a dict that mention all your family member ex:
# {'father' : 'Toni', 'mother' : 'Mimi', 'first_son' : 'Budi'}
#TODO Implement
family_dict = {'father' : 'Asep', 'mother' : 'Lia', 'first_son' : 'Hafiyyan'}

def index(request):
    response = {'family': family_dict}
    return render(request, 'index_lab2.html', response)