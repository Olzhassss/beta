from django.urls import path

from . import views
from .dash_apps import pieChart

app_name = 'stats'
urlpatterns = [
    path('', views.index, name='index'),
    path('pie-chart', views.PieChart_view, name='pieChart'),
    # path('apply', views.apply, name='application'),
    # path('applications/<int:app_id>/review', views.reviewApplication, name='appBrowse'),
    # path('applications/<int:app_id>/delete', views.deleteApplication, name='appDelete'),
    # path('applications', views.application_list_view, name='appList'),
    # path('administration/login', views.login, name='login'),
    # path('administration/register', views.register, name='register')
]