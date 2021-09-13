from django.shortcuts import render
from datetime import datetime, date

mhs_name = ''  # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date()  # TODO Implement this, format (Year, Month, Date)
npm = None  # TODO Implement this


def index(request):
    response = {'name': mhs_name,
                'age': calculate_age(birth_date.year),
                'npm': npm}
    return render(request, 'index_lab1.html', response)


def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0


def friend_list(request):
    friends = None  # TODO Implement this
    response = {'friends': friends}
    return render(request, 'friend_list_lab1.html', response)
