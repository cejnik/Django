from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:greet_number>', views.greet_number),
    path('<str:greet_string>', views.greet_string, name='greeting_string'),

]