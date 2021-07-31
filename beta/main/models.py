from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('Name', max_length=10)
    surname = models.CharField('Surname', max_length=10)

    def __str__(self):
        return self.name+' '+self.surname

    def get_absolute_url(self):
        return reverse("main:appBrowse", kwargs={"id": self.id})
    
    sex = models.CharField(max_length=6, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')])
    birth_year = models.SmallIntegerField()
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=25)
    # country = models.CharField(max_length=30)
    
    # # Education level field default
    # def simpleList(*args):
    #     for string in args:
    #         return (string.upper(), string)
    # ed_lvl_choices = simpleList(['Beginner', 'Elementary', 'Pre-Intermediate', 'Intermediate', 'Upper-Intermediate', 'Advanced'])
    # ed_lvl = models.CharField(max_length=25, choices=ed_lvl_choices)

    # class Meta:
    #     abstract = True
    