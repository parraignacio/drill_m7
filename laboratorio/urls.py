from django.urls import path
from . import views


urlpatterns = [
    path('insertar/', views.insertar_lab, name='insertar-lab'),
    path('', views.mostrar_lab, name='mostrar-lab'),
    path('editar/<int:pk>', views.editar_lab, name='editar-lab'),
    path('eliminar/<int:pk>', views.eliminar_lab, name='eliminar-lab'),
]
