from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Application(forms.Form):
    name = forms.CharField(label='Name', max_length=20)
    surname = forms.CharField(label='Surname', max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['name', 'surname']
        fields = list(map( lambda x: x.name, Profile._meta.get_fields()))

    # This overwrites classes in widget
    # def __init__(self, *args, **kwargs):
    #     super(forms.ModelForm, self).__init__(*args, **kwargs)
    #     # adding css classes to widgets without define the fields:
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = ' form-control'

    name = forms.SlugField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'col-3'}))

    def as_div(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)
        
