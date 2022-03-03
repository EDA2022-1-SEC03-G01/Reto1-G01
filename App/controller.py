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
 """

from nis import cat
from ossaudiodev import control_labels
import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def newController():
    """
    Crea una instancia del modelo
    """
    control={'model':None}
    control['model']=model.newCatalog()
    return control
# Inicialización del Catálogo de libros

# Funciones para la carga de datos
def loadData(control):
    catalog=control['model']
    artists=loadArtists(catalog)
    albums=loadAlbums(catalog)
    tracks=loadTracks(catalog)
    return artists,albums,tracks

def loadArtists(catalog):
    artistfile=cf.data_dir+'Spotify/spotify-artists-utf8-small.csv'
    input_file= csv.DictReader(open(artistfile,enconding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog,artist)
    return model.artistsSize(catalog)

def loadTracks(catalog):
    tracksFile=cf.data_dir+'Spotify/spotify-tracks-utf8-small.csv'
    input_file= csv.DictReader(open(tracksFile,encoding='utf-8'))
    for track in input_file:
        model.addTrack(catalog,track)
    return model.tracksSize(catalog)

def loadAlbums (catalog):
    albumsFile=cf.data_dir+'Spotify/spotify-albums-utf8-small.csv'
    input_file=csv.DictReader(open(albumsFile,encoding='utf-8'))
    for album in input_file:
        model.addAlbum(catalog,album)
    return model.albumsSize(catalog)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálog
