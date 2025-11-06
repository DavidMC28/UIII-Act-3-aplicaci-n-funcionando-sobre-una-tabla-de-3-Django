from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:pk>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),
]