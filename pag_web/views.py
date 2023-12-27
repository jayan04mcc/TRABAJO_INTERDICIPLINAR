from django.http import HttpResponse,JsonResponse
from .models import usuario,resultados
from django.shortcuts import render,redirect
from .form import RegistroForm
# Create your views here.
def index(request):
    return render(request, 'pag_web/index.html')

##ruta nueva
def view_indexnuevo(request):
    return render(request, 'pantallas_vista/index_nuevo.html')
def indexprueba(request):
    return render(request, 'pantallas_vista/indexprueba.html')

def view_index1(request):
    return render(request, 'pantallas_vista/index1.html')

def view_index2(request):
    return render(request, 'pantallas_vista/index2.html')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print("Valido")
            form.save()
            return redirect('ruta_indexnuevo')
        else:
            print("Formulario no válido")
            print(form.errors)
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

