﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de artistas y obras

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en la
    estructura de datos
    """
    loadArtistas(catalog)
    loadObras(catalog)
    
    
    

def loadArtistas(catalog):
    """
    Carga los artistas del archivo y los agrega a la lista de artistas.
    """
    artistsFile = cf.data_dir + 'GoodReads/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsFile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadObras(catalog):
    """
    Carga todos laas obras del archivo y los agrega a la lista de obras.
    """
    artworksFile = cf.data_dir + 'GoodReads/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksFile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


# Funciones de ordenamiento

def ordenarListaC(label1, label2, catalog):
    """
    Ordena los artistas en lista cronologica
    """
    lista = model.ordenarListaC(label1, label2, catalog)
    return lista

def sortObrasA(catalog):
    """
    Ordena las obras en orden de adquisición
    """
    model.sortObrasA(catalog)

def sortObrasAT(catalog):
    """
    Ordena las obras por la técnica de su creador
    """
    model.sortObrasAT(catalog)

def sortObrasAN(catalog):
    """
    Ordena las obras por la nacionalidad de su creador
    """
    model.sortObrasAN(catalog)

def transladoO(label, catalog):

    lista = model.transladarO(label, catalog)

    return lista



def darNObrasArtista(catalog, label):

    f = model.darNObrasArtista(catalog, label)

    return f








