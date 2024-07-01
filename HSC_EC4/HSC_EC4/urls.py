from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('integrantes/', views.integrantes, name = "integrantes"),
    path('saludo/', views.saludo, name = "saludo"),
    ]