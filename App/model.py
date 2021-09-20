"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from typing import TYPE_CHECKING
import config as cf
import datetime
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artist': None,
               'artwork': None}

    catalog['artist'] = lt.newList('ARRAY_LIST')
    catalog['artwork'] = lt.newList('ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    """
    Adiciona un artista a la lista de artistas
    """
    a = newArtist(artist['ConstituentID'],artist['DisplayName'],
                  artist['ArtistBio'],artist['Nationality'],
                  artist['Gender'],artist['BeginDate'],
                  artist['EndDate'],artist['Wiki QID'],
                  artist['ULAN'])
    lt.addLast(catalog['artist'], a)

def addArtwork(catalog, artwork):
    """
    Adiciona un artista a la lista de artistas
    """
    ar = newArtwork(artwork['ObjectID'],artwork['Title'],
                    artwork['ConstituentID'],artwork['Date'],
                    artwork['Medium'],artwork['Dimensions'],
                    artwork['CreditLine'],artwork['AccessionNumber'],
                    artwork['Classification'],artwork['Department'],
                    artwork['DateAcquired'],artwork['Cataloged'],
                    artwork['URL'],artwork['Circumference (cm)'],
                    artwork['Depth (cm)'],artwork['Diameter (cm)'],
                    artwork['Height (cm)'],artwork['Length (cm)'],
                    artwork['Weight (kg)'],artwork['Width (cm)'],
                    artwork['Seat Height (cm)'],artwork['Duration (sec.)'])
    lt.addLast(catalog['artwork'], ar)

    #artists = artwork['ConstituentID']

    #for artist in artists:
     #   addArtworkArtist(catalog, artist.strip(), artwork)

# Funciones para creacion de datos

def newArtist(constituentID, displayName, artistBio, nationality, 
              gender, beginDate, endDate, wikiQID, ulan):
    """
    Esta estructura almancena los artistas.
    """
    artist = {'ConstituentID': '', 'DisplayName': '','ArtistBio': '',
           'Nationality': '', 'Gender': '', 'BeginDate': '', 'EndDate': '',
           'Wiki QID': '', 'ULAN': ''}
    artist['name'] = constituentID
    artist['DisplayName'] = displayName
    artist['ArtistBio'] = artistBio
    artist['Nationality'] = nationality
    artist['Gender'] = gender
    artist['BeginDate'] = beginDate
    artist['EndDate'] = endDate
    artist['Wiki QID'] = wikiQID
    artist['ULAN'] = ulan
    return artist
    
def newArtwork(objectID, title, constituentID, date, medium, dimensions, creditLine,
               accessionNumber, classification, department, dateAdquired, cataloged,
               url, circumference, depth, diameter, height, length, weight, width,
               seatHeight, duration):
    """
    Esta estructura almancena los artistas.
    """
    artwork = {'ObjectID': '', 'Title': '','ConstituentID': '',
           'Date': '', 'Medium': '', 'Dimensions': '', 'CreditLine': '',
           'AccessionNumber': '', 'Classification': '', 'Department': '', 
           'DateAcquired': '','Cataloged': '', 'URL': '', 'Circumference (cm)': '', 
           'Depth (cm)': '', 'Diameter (cm)': '', 'Height (cm)': '', 'Length (cm)': '',
           'Weight (kg)': '', 'Width (cm)': '', 'Seat Height (cm)': '', 'Duration (sec.)': ''}
    artwork['ObjectID'] = objectID
    artwork['Title'] = title
    artwork['ConstituentID'] = constituentID
    artwork['Date'] = date
    artwork['Medium'] = medium
    artwork['Dimensions'] = dimensions
    artwork['CreditLine'] = creditLine
    artwork['AccessionNumber'] = accessionNumber
    artwork['Classification'] = classification
    artwork['Department'] = department
    artwork['DateAcquired'] = dateAdquired
    artwork['Cataloged'] = cataloged
    artwork['URL'] = url
    artwork['Circumference (cm)'] = circumference
    artwork['Depth (cm)'] = depth
    artwork['Diameter (cm)'] = diameter
    artwork['Height (cm)'] = height
    artwork['Length (cm)'] = length
    artwork['Weight (kg)'] = weight
    artwork['Width (cm)'] = width
    artwork['Seat Height (cm)'] = seatHeight
    artwork['Duration (sec.)'] = duration
    
    return artwork
    

# Funciones de consulta
def consultaañoartista (artista):
    año = artista['BeginDate']
    return año



# Funciones utilizadas para comparar elementos dentro de una lista
def compareBeginDate1 (artista, año, añof):
    añoc = int(artista['BeginDate'])
    if (año == añoc):
        return 1
    elif (año > añoc):
        return 0
    elif (año < añoc):
        if añof == añoc:
            return 1
        elif añof > añoc:
            return 1
        else:
            return 0



def getNumero():
    b = 2-1
    c = str(b)
    a = int(c)
    return a


def compareBeginDate(artist1, artist2):
    cadena1 = artist1['BeginDate']
    año1 = cadena1[:4]
    mes1 = cadena1[5:7]
    dia1 = cadena1[-2:]

    cadena2 = artist2['BeginDate']
    año2 = cadena2[:4]
    mes2 = cadena2[5:7]
    dia2 = cadena2 [-2:]

    if año1 > año2:
        return 1
    elif año1 == año2:
        if mes1 > mes2:
            return 1
        elif mes1 == mes2:
            if dia1>dia2:
                return 1 
            elif dia1 == dia2:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1

def compareDate(artwork1, artwork2):
    cadena1 = artwork1['Date']
    
    cadena2 = artwork2['Date']
    
    if  cadena1 > cadena2:
        return 1
    elif cadena1 < cadena2:
        return -1
    else:
        return 0
     
            


# Funciones de ordenamiento


def ordenarListaC(añoi, añof, catalog):
    lista = lt.newList('ARRAY_LIST')
    lista1 = lista_artistasC(añoi, añof, catalog)
    lista2 = lista_artistasCR(añoi, añof, catalog)
    for i in lista2:
        for j in lista1:
            if lista2[i] == lista1[int(j['BeginDate'])]:
                lt.addLast(lista, j)
    return lista


def lista_artistasC(añoi, añof, catalog):
    lista = lt.newList('ARRAY_LIST')
    for artist in catalog:
        valor = compareBeginDate1 (artist, añoi, añof)
        if valor == 1:
            lt.addLast(artist)
            
    
    return lista


def lista_artistasCR(añoi, añof, catalog):
    lista = lt.newList('ARRAY_LIST')
    for artist in catalog:
        valor = compareBeginDate1 (artist, añoi, añof)
        if valor == 1:
            lt.addLast(int(artist['BeginDate']))
    lista.sort()
    return lista




            
                