from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [10,20]</a>
        </li>
        <li>
            <a href="/rango2"> Mostrar Números [a,b]</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    mensaje="""
        <h1>Inicio</h1>
    """
    return HttpResponse(layout + mensaje)


def saludo(request):
    mensaje = """
        <h1>Bienvenidos</h1>
        <h2>Flor Cerdán</h2>
        <h3>Python....</h3>
    """
    return HttpResponse(layout + mensaje)


def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)


def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)

