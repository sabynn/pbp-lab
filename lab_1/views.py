from django.shortcuts import render

#Enter Your Name Here
mhs_name = '' # TODO IMPLEMENT

# Create your views here.
def index(request):


    response = {'name' : mhs_name}
    return render(request,'index.html',response)