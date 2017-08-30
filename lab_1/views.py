from django.shortcuts import render
from datetime import datetime
# Enter your name here
mhs_name = '' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_year = curr_year #TODO Implement this
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_year)}
    return render(request, 'index.html', response)


def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
