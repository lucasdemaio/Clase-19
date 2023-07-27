from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader


def saludo(request):
    return HttpResponse("Hola")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    texto = f"Hoy es {dia}"
    
    mihtml = open("C:/Users/Lucas/Downloads/Python/Clase 18/proyecto/Plantillas/template1.html")
    
    plantilla = Template(mihtml.read())
    mihtml.close()

    micontexto = Context(texto)

    documento = plantilla.render(micontexto)

    return HttpResponse(documento)


def miNombreEs(self, nombre):
    texto = f"Mi nombre es {nombre}"

    return HttpResponse(texto)

def probandotemplate(self):
    nom = "Lucas"
    ap = "De Maio"

    listanotas = [4,3,8,2,9,10]
    
    diccionario = {"nombre":nom, "apellido":ap, "fecha_hoy": datetime.datetime.now, "notas": listanotas}

    #mihtml = open("C:/Users/Lucas/Downloads/Python/Clase 18/proyecto/Plantillas/template1.html")

    plantilla = loader.get_template('template1.html')
    #mihtml.close()
    #micontexto = Context(diccionario)

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)








