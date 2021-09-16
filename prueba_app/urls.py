"""Perfil employees"""

from django.contrib import admin
from django.urls import path
from employees import views as employees_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('employees/',)
]
