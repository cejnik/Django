from django.urls import path
from . import views

urlpatterns = [
    path('<teachername>', views.allteachersinfo)
]
