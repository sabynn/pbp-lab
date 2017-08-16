from django.shortcuts import render

mhs_name = 'Hafiyyan' #Enter Your Name Here

# Create your views here.
def index(request):

    # TODO IMPLEMENT
    response = {'name' : mhs_name}
    return render(request,'index.html',response)