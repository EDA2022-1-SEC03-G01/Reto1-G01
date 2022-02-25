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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar los álbunes en un periodo de tiempo")
    print("3- Encontrar los artistas más populares")
    print("4- Encontrar las canciones más populares")
    print("5- Encontrar la canción más popular de un artista")
    print("6- Encontar la discografía de un artista")
    print("7- Clasificar las canciones con mayor distribución")
    print("0- Salir")

def loadData():
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    artists, albums, tracks = controller.loadData(control)
    return artists, albums, tracks 

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        artist,albums,tracks=loadData()
    elif int(inputs[0]) == 2:
        p_tiempo=input('Ingrese el periodo de tiempo del cual desea listar los albunes: ')
        print('Linstando albunes...')
    elif int(inputs[0])==3:
        print('Encontrando los artistas mas populares...')
    elif int(inputs[0])==4:
        print('Encontrando las canciones mas populares...')
    elif int(inputs[0])==5:
        artista=input('Ingrese el nombre del artitas del que desea saber su cancion mas popular: ')
        print('Encontrando la cancion mas popular del artista...')
    elif int(inputs[0])==6:
        artista=input('Ingrese el nombre del artitas del que desea saber su discografia: ')
        print('Encontrando la discografia del artista...')
    elif int(inputs[0])==7:
        print('Clasificando las canciones con mayor distribución...')
    else:
        sys.exit(0)
sys.exit(0)
