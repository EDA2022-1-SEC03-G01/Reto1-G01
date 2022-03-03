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


from gettext import Catalog
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog={'artist':None,'albums':None,'tracks':None}
    catalog['artist']=lt.newList('ARRAY_LIST')
    catalog['albums']=lt.newList('ARRAY_LIST')
    catalog['tracks']=lt.newList('ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo
def addTrack(catalog,track):
    lt.addLast(catalog['tracks'],track)
    artists=track['artists'].split(",")
    for artist in artists:
        addArtist(catalog,artist.strp(),track)
    return catalog

def addArtist(catalog,artistName,):
    artists=catalog['artists']
    posArtist=lt.isPresent(artists,artistName)
    if posArtist > 0:
        artist = lt.getElement(artists, posArtist)
    else:
        artist = newArtist(artistName)
        lt.addLast(artists, artist)
    #Aca añadir las sublistas necesarias de los artistas
    return catalog

def addAlbum(catalog,album):
    albums=catalog['albums']
    t=newAlbum(album['album_name'],)


# Funciones para creacion de datos

# Funciones de consulta
def tracksSize(catalog):
    return lt.size(catalog['books'])

def albumsSize(catalog):
    return lt.size(catalog['albums'])

def artistsSize(catalog):
    return lt.size(catalog['artist'])
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento