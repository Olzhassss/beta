from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, ListView, DeleteView

from random import randint, choice
from .models import Profile
from .forms import ProfileForm, RegisterForm

from .static.main.scripts.generator import generate_word, generate_phone_number, generate_email

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def apply(request):
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         surname = form.cleaned_data['surname']
    names = {
        'name': generate_word(randint(4,10)).capitalize(),
        'surname': generate_word(randint(4,10)).capitalize(),
        'sex': choice(['FEMALE', 'MALE']),
        'birth_year': randint(1950,2005),
        'phone_number': generate_phone_number(),
        'email': generate_email(10),
        # 'country': ,
    }

    form = ProfileForm(request.POST or None, initial=names)
    if form.is_valid():
        form.save()
        form = ProfileForm(initial=names)

    context = {
        'form': form
    }
    return render(request, 'main/application.html', context)


# def deleteApplication(request, app_id):
#     obj = get_object_or_404(Profile, id=app_id)

#     if request.method == 'POST':
#         obj.delete()
#         return redirect('main:appList')

#     context = { 'obj':obj }
#     return render(request, 'main/appDelete.html', context)

class AppDelete_view(DeleteView):
    template_name = 'main/appDelete.html'

    def get_object(self):
        id_ = self.kwargs.get('app_id')
        return get_object_or_404(Profile, id=id_)

    def get_success_url(self):
        return reverse('main:appList')

def reviewApplication(request, app_id):
    obj = get_object_or_404(Profile, id=app_id)
    obj_dict = dict(map( lambda x: (x.verbose_name, x.value_to_string(obj)), Profile._meta.get_fields()))
    context = { 'obj':obj_dict }
    return render(request, 'main/appBrowse.html', context)


class AppList_view(ListView):
    model = Profile
    template_name = 'main/appList.html'

# def application_list_view(request):
#     queryset = Profile.objects.all()
#     context = { 'obj_list':queryset }
#     return render(request, 'main/appList.html', context)


def login(request):
    context = {}
    return render(request, 'main/login.html')


def register(request):
    form = RegisterForm()


    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()

    context = {'form':form}
    return render(request, 'main/register.html', context)