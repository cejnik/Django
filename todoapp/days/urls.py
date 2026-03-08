from django.urls import path
from . import views

urlpatterns = [
    path('<int:dayinweek_number>', views.daynumber),
    path('<str:dayinweek_string>', views.daytext),

]