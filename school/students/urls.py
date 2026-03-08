# URLS in apps students
from django.urls import path # doplněno
from . import views #doplněno

urlpatterns = [
    # path ('martin', views.martinstudent),
    path('<studentsname>', views.allstudentsinfo),
]