from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from comodidades.models import Comodidad  

def comodidades(request):  
    comodidades_list = Comodidad.objects.all()  
    return render(request, 'comodidades/index.html', {'comodidades_list': comodidades_list})

def change_status_comodidad(request, comodidad_id):
    comodidad = Comodidad.objects.get(pk=comodidad_id)
    comodidad.status = not comodidad.status
    comodidad.save()
    return redirect('comodidades')  






