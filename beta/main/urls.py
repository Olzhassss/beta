from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('apply', views.apply, name='application'),
    path('applications/<int:app_id>/review', views.reviewApplication, name='appBrowse'),
    path('applications/<int:app_id>/delete', views.AppDelete_view.as_view(), name='appDelete'),
    path('applications', views.AppList_view.as_view(), name='appList'),
    path('administration/login', views.login, name='login'),
    path('administration/register', views.register, name='register')
]