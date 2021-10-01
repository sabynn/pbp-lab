from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from lab_1.models import Friend
from lab_3.forms import FriendForm


# Create your views here.
@login_required(login_url='/admin/login/')


def index(request):
    friends = Friend.objects.all()
    response = {'friends': friends}
    return render(request, 'lab3_index.html', response)


def add_friend(request):
    form = FriendForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/lab-3")
    response = {'form': form}
    return render(request, 'lab3_form.html', response)
