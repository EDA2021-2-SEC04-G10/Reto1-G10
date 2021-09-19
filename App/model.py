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
                    artwork['DateAdquired'],artwork['Cataloged'],
                    artwork['URL'],artwork['Circumference(cm)'],
                    artwork['Depth(cm)'],artwork['Diameter(cm)'],
                    artwork['Height(cm)'],artwork['Length(cm)'],
                    artwork['Weight(kg)'],artwork['Width(cm)'],
                    artwork['Seat Height(cm)'],artwork['Duration(sec.)'])
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
           'DateAdquired': '','Cataloged': '', 'URL': '', 'Circumference(cm)': '', 
           'Depth(cm)': '', 'Diameter(cm)': '', 'Height(cm)': '', 'Length(cm)': '',
           'Weight(kg)': '', 'Width(cm)': '', 'Seat Height(cm)': '', 'Duration(sec.)': ''}
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
    artwork['DateAdquired'] = dateAdquired
    artwork['Cataloged'] = cataloged
    artwork['URL'] = url
    artwork['Circumference(cm)'] = circumference
    artwork['Depth(cm)'] = depth
    artwork['Diameter(cm)'] = diameter
    artwork['Height(cm)'] = height
    artwork['Length(cm)'] = length
    artwork['Weight(kg)'] = weight
    artwork['Width(cm)'] = width
    artwork['Seat Height(cm)'] = seatHeight
    artwork['Duration(sec.)'] = duration
    
    return artwork
    

# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista

def compareBeginDate(artist1, artist2):
    x = artist1['BeginDate'].datetime()
    if (artist1['BeginDate'] == artist2['BeginDate']):
        return 0
    elif (artist1['BeginDate'] > artist2['BeginDate']):
        return 1
    return -1

def compareratings(book1, book2):
    return (date(book1['average_rating']) > float(book2['average_rating']))


# Funciones de ordenamiento