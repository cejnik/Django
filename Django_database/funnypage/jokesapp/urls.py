from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('thank-you', views.thank_you, name='thank_you_page'),
    path('all-jokes', views.all_jokes, name='all_jokes_page'),
]
