from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Deposito, Retiro

def index(request):
    return render(request, 'registro/index.html')

def clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        fechanacimiento = request.POST.get('fechanacimiento')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')

        c = Cliente(nombre=nombre, apellido=apellido, direccion=direccion, fechanacimiento=fechanacimiento, telefono=telefono, correo=correo)
        c.save()  #Se realiza un insert a la BD

        messages.add_message(request, messages.INFO, f'El cliente {nombre} {apellido} ha sido registrado con éxito')
    
    activo = 'clientes'
    q = request.GET.get('q')

    if q:
        data = Cliente.objects.filter(nombre__startswith=q).order_by('nombre')

        '''
            select * 
            from clientes
            where nombre like 'n%'
        '''
    else:
        data = Cliente.objects.all().order_by('nombre')

    ctx = {
        'activo' : activo,
        'clientes': data,
        'q': q
    }

    return render(request, 'registro/clientes.html', ctx)

def depositos(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        saldo = request.POST.get('saldo')
        cliente = request.POST.get('cliente')

        d = Deposito(cantidad=cantidad, saldo=saldo, cliente=cliente)
        d.save()  #Se realiza un insert a la BD

        messages.add_message(request, messages.INFO, f'Ha sido depositado con éxito')
    
    activo = 'depositos'
    q = request.GET.get('q')

    if q:
        data = Deposito.objects.filter(nombre__startswith=q)

        '''
            select * 
            from depositos
            where cliente like 'n%'
        '''
    else:
        data = Deposito.objects.all()

    ctx = {
        'activo' : activo,
        'depositos': data,
        'q': q
    }

    return render(request, 'registro/depositos.html', ctx)

def retiros(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        saldo = request.POST.get('saldo')
        cliente = request.POST.get('cliente')

        d = Retiro(cantidad=cantidad, saldo=saldo, cliente=cliente)
        d.save()  #Se realiza un insert a la BD

        messages.add_message(request, messages.INFO, f'Ha retirado con éxito')
    
    activo = 'retiros'
    q = request.GET.get('q')

    if q:
        data = Retiro.objects.filter(nombre__startswith=q)

        '''
            select * 
            from retiros
            where cliente like 'n%'
        '''
    else:
        data = Retiro.objects.all()

    ctx = {
        'activo' : activo,
        'retiross': data,
        'q': q
    }

    return render(request, 'registro/depositos.html', ctx)


