﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from DISClib.DataStructures.arraylist import addLast
from os import umask
import config as cf
import sys
import controller
import datetime
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista cronologica de artistas")
    print("3- Lista cronologica de las adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- Clasificar las obras por la nacionalidad de su creador")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo de artistas y obras
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los artistas y obras en la estructura de datos
    """
    controller.loadData(catalog)


catalog = None

def printAuthorData(artist):
    if artist:
        print('Autor encontrado: ' + artist['ConstituentID'])
        print('Promedio: ' + str(artist['DisplayName']))
        print('Total de libros: ' + str(lt.size(artist['BeginDate'])))
        
    else:
        print('No se encontro el autor')


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artist'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artwork'])))
    elif int(inputs[0]) == 2:
        label1 = input("Introduzca Año Inicial:")
        label2 = input("Introduzca Año Final:")
        lista = controller.ordenarListaC(int(label1), int(label2), catalog)
        print ("El número total de artistas nacidos entre " + label1 + "y " + label2 + "es: " + len(lista))
        print("Tres primeros y tres ultimos por orden cronologico ")
        punta = 1
        while punta < 4:
            print("Nombre del artista: " + lista[punta].get('DisplayName') )
            print("Año de nacimiento: " + lista[punta].get('BeginDate'))
            print ("Año de nacimiento: " + lista[punta].get('BeginDate'))
            print ("Año de fallecimiento: " + lista[punta].get('EndDate'))
            print ("Nacionalidad: " + lista[punta].get('Nationality'))
            print ("Género: " + lista[punta].get('Gender'))
            punta +=1
        cola = len(lista)
        while cola > len(lista)-3:
            print("Nombre del artista: " + lista[punta].get('DisplayName') )
            print("Año de nacimiento: " + lista[punta].get('BeginDate'))
            print ("Año de nacimiento: " + lista[punta].get('BeginDate'))
            print ("Año de fallecimiento: " + lista[punta].get('EndDate'))
            print ("Nacionalidad: " + lista[punta].get('Nationality'))
            print ("Género: " + lista[punta].get('Gender'))
            cola -=1
    
    elif int(inputs[0]) ==3:
        label1 = input("Introduzca Fecha Inicial:")
        label2 = input("Introduzca Fecha Final:")
        lista = controller.ordenarListaC((label1), (label2), catalog)
        print ("El número total de obras adquiridas entre " + label1 + "y " + label2 + "es: " + len(lista))
        i = 1
        listap = lt.newList('ARRAY_LIST')
        for i in lista: 
            if str(lista[i].get('DateAcquired')=='purchase'):
                addLast(listap, lista[i])
        print("El número total de obras adquiridas por 'purchase' son: " + len(listap))
        punta = 1
        while punta < 4:
            print("Nombre de la obra: " + lista[punta].get('Title') )
            
            print("Artistas: " + lista[punta].get('BeginDate'))
            print ("Año de nacimiento: " + lista[punta].get('BeginDate'))
            print ("Año de fallecimiento: " + lista[punta].get('EndDate'))
            print ("Nacionalidad: " + lista[punta].get('Nationality'))
            print ("Género: " + lista[punta].get('Gender'))
            punta +=1
        cola = len(lista)
        while cola > len(lista)-3:
            print("Nombre del artista: " + lista[punta].get('DisplayName') )
            print("Año de nacimiento: " + lista[punta].get('BeginDate'))
            print ("Año de nacimiento: " + lista[punta].get('BeginDate'))
            print ("Año de fallecimiento: " + lista[punta].get('EndDate'))
            print ("Nacionalidad: " + lista[punta].get('Nationality'))
            print ("Género: " + lista[punta].get('Gender'))
            cola -=1






            
        print(lista)
    elif int(inputs[0]) ==4:
        label = input("Introduzca Nombre del Artista: ")
        resultado = controller.darNObrasArtista(catalog, str(label))
        print(resultado)
    elif int(inputs[0]) == 5:
        authorname = input("Nombre del autor a buscar: ")
        author = controller.getBooksByAuthor(catalog, authorname)
        printAuthorData(author)
    
    
        
    elif int(inputs[0]) == 5:
        label = input("Introduzca departamento de transferencia:\n ")
        lista = controller.transladoO(str(label), catalog)
        print('Total de obras a transportar:')
        print(str(lt.size(lista)))
                
        

    else:
        sys.exit(0)
sys.exit(0)
