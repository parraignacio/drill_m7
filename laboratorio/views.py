from django.shortcuts import render, redirect
from .models import Laboratorio, DirectorGeneral, Producto

def insertar_lab(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        
        return redirect('mostrar-lab')
    else:
        return render(request, 'insertar.html')

def mostrar_lab(request):
    contador = request.session.get('contador', 0)
    contador += 1
    request.session['contador'] = contador
    
    laboratorios = Laboratorio.objects.all()
    return render(request, 'mostrar.html', {'laboratorios': laboratorios, 'contador': contador})

def editar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        
        laboratorio.nombre = nombre
        laboratorio.ciudad = ciudad
        laboratorio.pais = pais
        laboratorio.save()
        
        return redirect('mostrar-lab')
    
    return render(request, 'editar.html', {'laboratorio': laboratorio})

def eliminar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar-lab')

    return render(request, 'eliminar.html', {'laboratorio': laboratorio})