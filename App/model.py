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

from multiprocessing.dummy import Array

from numpy import array, imag
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog() -> None:
    '''
    Incializa el catalogo de libros. Crea una lista vacia paraguardar
    todos los libros, adicionalmente, crea una lista vacia para los artistas,
    los albumes y las canciones
    Retorna:
        dict: retorna el catalogo con las listas inicializadas
    '''
    catalog={'artist':None,'albums':None,'tracks':None}
    catalog['artist']=lt.newList('ARRAY_LIST')
    catalog['albums']=lt.newList('ARRAY_LIST')
    catalog['tracks']=lt.newList('ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo
def addTrack(catalog: dict,trackName: str):
    tracks=catalog['tracks']
    posTrack=lt.isPresent(tracks,trackName)
    if posTrack > 0:
        track=lt.getElement(tracks,trackName)
    else:
        track=newTrack(trackName)
        lt.addLast(tracks,track)

def addArtist(catalog: dict,artistName: str):
    artists=catalog['artists']
    posArtist=lt.isPresent(artists,artistName)
    if posArtist > 0:
        artist = lt.getElement(artists, posArtist)
    else:
        artist = newArtist(artistName)
        lt.addLast(artists, artist)
    #Aca añadir las sublistas necesarias de los artistas
    return catalog

def addAlbum(catalog: dict,albumName:str) ->None:
    albums=catalog['albums']
    t=newAlbum(catalog, albumName)

# Funciones para creacion de datos
def newArtist(artist_popularity: float,followers: int,genres: str,id:str,name:str,track_id:str):
    artist={'artist_popularity':0,'followers':0,'genres':"",'id':"",'name':"",'track_id':""}
    artist['name'] =name
    artist['albums']=lt.newList('ARRAY_LIST')
    return artist

def newAlbum(album_type: str,artist_id: str,avaible_markets: lt,external_urls: str,id:str,images: lt,name:str,release_date: str, total_track: int,track_id:str):
    album={'album_type':"",'artist_id':"",'avaible_markets':None,'external_urls':"",'id':"",'images':None,'name':"",'release_date':"",'total_tracks':0,'track_id':""}
    album['album_type']=album_type
    album['artist_id']=artist_id
    album['avaible_markets']=avaible_markets
    album['external_urls']=external_urls
    album['id']=id
    album['images']=images
    album['name']=name
    album['release_date']=release_date
    album['total_track']=total_track
    album['track_id']=track_id

def newTrack(catalog: dict, trackName: str):
    pass

# Funciones de consulta
def tracksSize(catalog: dict) -> int:
    return lt.size(catalog['books'])

def albumsSize(catalog: dict) -> int:
    return lt.size(catalog['albums'])

def artistsSize(catalog:dict) -> int:
    return lt.size(catalog['artist'])

# Funciones utilizadas para comparar elementos dentro de una lista
def compareArtist(artistName: int,artist: dict):
    if artistName.lower()==artist['name'].lower():
        return 0
    elif artistName.lower()>artist['name'].lower():
        return 1
    else:
        return -1
def comparAlbums(albumId, album):
    pass
# Funciones de ordenamiento