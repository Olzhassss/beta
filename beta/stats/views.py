from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


from random import randint, choice
from main.models import Profile

# Create your views here.
def index(request):
    return render(request, 'stats/index.html')


def PieChart_view(request):
    return render(request, 'stats/pieChart.html')


def reviewApplication(request, app_id):
    obj = get_object_or_404(Profile, id=app_id)
    obj_dict = dict(map( lambda x: (x.verbose_name, x.value_to_string(obj)), Profile._meta.get_fields()))
    context = { 'obj':obj_dict }
    return render(request, 'main/appBrowse.html', context)


def application_list_view(request):
    queryset = Profile.objects.all()
    context = { 'obj_list':queryset }
    return render(request, 'main/appList.html', context)