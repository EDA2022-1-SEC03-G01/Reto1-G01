"""
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

from ssl import ALERT_DESCRIPTION_CLOSE_NOTIFY
from tempfile import _TemporaryFileWrapper
from typing import Dict
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
    print("2- Listar los albunes en un periodo de tiempo")
    print("3- Encontrar los artistas mas populares")
    print("4- Clasificar las canciones por popularidad")
    print("5- Encontrar la cancion mas popular de un artista")
    print("6- Encontrar la discografica de un artista")
    print("7- Clasificar las canciones con mayor distribucion")
    print("0- Salir")

def loadData():
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    artists, albums, tracks = controller.loadData(control)
    return artists, albums, tracks 

def printAlbumsInPeriod(albums: lt)-> None:
    pass

def printTopArtist(artist: lt)->None:
    pass

def printTopTracks(tracks: lt) -> None:
    pass

def printArtistPopularTrack(track: dict) -> None:
    pass

def printArtistDiscography(discography: lt) -> None:
    pass

def printMostDistributedTracks(tracks: lt)-> None:
    pass


catalog = None
control=newController()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        artists, albums, tracks = loadData()
        print('Artistas cargados: ' + str(artists))
        print('Albunes cargados: ' + str(albums))
        print('Caciones cargadas: ' + str(tracks))
    elif int(inputs[0]) == 2:
        intialY = input("Ingrese el año inicial del periodo (con formato AAAA): ")
        finalY= input("Ingrese el año final de periodo (con formato AAAA): ")
        print('Listando los albunes del periodo de tiempo... ')
        albums = controller.getAlbumsInPeriod(control, int(intialY),int(finalY))
        printAlbumsInPeriod(albums)
    elif int(inputs[0]) == 3:
        top = input("Ingrese el tamaño del grupo de artistas a encontrar: ")
        print('Encontrando los '+top+' artistas más populares...')
        topArtist = controller.getTopArtist(control, int(top))
        printTopArtist(topArtist)
    elif int(inputs[0]) == 4:
        top = input("Ingrese el número de canciones que desea encontrar: ")
        print('Encontrando las '+top+ " canciones mas populares...")
        topTracks = controller.getTopTracks(control, int(top))
        printTopTracks(topTracks)
    elif int(inputs[0]) == 5:
        artistName=input("Ingrese el nombre del artista: ")
        print('Encontrando la cancion mas popular de '+ artistName + ' ...')
        popularTrack=controller.getArtistPopularTrack(control,artistName)
        printArtistPopularTrack(popularTrack)
    elif int(inputs[0]) == 6:
        artistName=input('Ingrese el nombre del artista: ')
        print('Encontrando la discografia de '+artistName+' ...')
        artistDiscography=controller.getArtistDiscography(control, artistName)
        printArtistDiscography(artistDiscography)
    elif int(inputs[0]) == 7:
        initialY=input("Ingrese el año inicial del periodo (con formato AAAA): ")
        finalY=input("Ingrese el año final de periodo (en formato AAAA): ")
        print("Clasificando las canciones con mayor distribucion...")
        mostDistrTracks=controller.getMostDistributedTracks(control,int(initialY),int(finalY))
        printMostDistributedTracks(mostDistrTracks)
    elif int(inputs[0]) == 0:
        sys.exit(0)   
    else:
        continue
sys.exit(0)
