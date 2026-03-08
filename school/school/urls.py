# URLS in config directory School
from django.contrib import admin
from django.urls import path, include #doplněno include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls'))
]
