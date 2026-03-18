from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:dayinweek_number>', views.daynumber),
    path('<str:dayinweek_string>', views.daytext, name='days_tasks'),

]