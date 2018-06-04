# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:42:23 2018

@author: adri8
"""
import pandas
import os


def cargaDfClima(walkDirClima, lstCabeceras, weatherStation):
    #cabeceras = ['Estación','Provincia','Temperatura máxima (ºC)','Temperatura mínima (ºC)','Temperatura media (ºC)','Racha (km/h)','Velocidad máxima (km/h)','Precipitación 00-24h (mm)','Precipitación 00-06h (mm)','Precipitación 06-12h (mm)','Precipitación 12-18h (mm)','Precipitación 18-24h (mm)']
    dfTotal = pandas.DataFrame(columns=lstCabeceras)
    """rutaActual = os.path.dirname(os.path.abspath(__file__)) +'\datos\datos2017'
    #hay que salir de lib y entrar en datos
    rutaActual = os.path.dirname(os.path.abspath(__file__))
    rutaDatosClima = rutaActual[:-4] +'\datos\datos2016'
    path = rutaDatosClima 
    #rutaXls = rutaDatosClima + chr(92) + chr(92)"""
    rutaXls = walkDirClima + os.sep
    
    #Lista vacia para incluir los ficheros
    #lstFiles = [] 
    for root, dirs, files in os.walk(walkDirClima,topdown=False):
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ".xls"):
                #lstFiles.append(nombreFichero+extension)
                #aqui podemos ir juntando el dato que leemos
                dfAuxClima = pandas.read_excel(rutaXls + nombreFichero+extension,skiprows=4)
                #dfAuxRetiro = dfAuxClima.loc[dfAuxClima['Estación'] == 'Madrid, Retiro']
                dfAuxRetiro = dfAuxClima.loc[dfAuxClima['Estación'] == weatherStation]
                dfTotal=pandas.concat([dfTotal, dfAuxRetiro])
    #en dfTotal tenemos todos los datos del clima de la estación del retiro
    return dfTotal

#funcion para quitar la hora cuando importo el xls del clima
def quitarHora(cadena):
    if type(cadena) is str:
        if (len(cadena)>8):
            cadena=cadena[:-8]
    return cadena    

#dfPruebaClima = cargaDfClima('ruta',['lista de cabeceras'],'nombre de la estacion')
    