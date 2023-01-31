from django.contrib import admin
from django.urls import path, include
from crudapp.api.views import get_list, get_details


urlpatterns = [
    path('list/', get_list, name='animal-list'),
    path('list/<int:pk>/', get_details, name='animal-details'),

]
