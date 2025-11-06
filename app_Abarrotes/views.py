from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm # Lo crearemos a continuación

def inicio(request):
    return render(request, 'inicio.html')

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES) # Es importante incluir request.FILES
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/agregar_empleado.html', {'form': form})

def actualizar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado) # También request.FILES
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/actualizar_empleado.html', {'form': form})

def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})