from django.shortcuts import render,redirect
from .forms import GeneroForms

def Home(request):
    return render(request,'index.html')

def CrearGenero(request):
    if request.method=='POST':
        genero_forms=GeneroForms(request.POST)
        if genero_forms.is_valid():
            genero_forms.save()
            return redirect('index')
    else :
        genero_forms=GeneroForms()
        return render(request,'crear_genero.html',{'autor_form':genero_forms})