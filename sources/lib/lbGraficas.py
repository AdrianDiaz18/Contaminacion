# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:51:57 2017

@author: adri8
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np

#dataset = pandas.read_csv('datos/international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
#plt.plot(dataset)
#plt.show()

def cargaDataSet(dirArchivo):
    dfContaminacion = pandas.DataFrame(columns = ["Estacion","Magnitud","Tecnica","Periodo_Analisis","Año","Mes","Dia1","Dia2","Dia3","Dia4","Dia5","Dia6","Dia7","Dia8","Dia9","Dia10","Dia11","Dia12","Dia13","Dia14","Dia15","Dia16","Dia17","Dia18","Dia19","Dia20","Dia21","Dia22","Dia23","Dia24","Dia25","Dia26","Dia27","Dia28","Dia29","Dia30","Dia31"])
    dfTxtCont = pandas.read_csv(dirArchivo,names=['col'])
    for r in range (0,len(dfTxtCont.index.values),1):
        l = []
        l.append(dfTxtCont['col'][r][0:8])     # Estacion
        l.append(dfTxtCont['col'][r][8:10])    # Magnitud
        l.append(dfTxtCont['col'][r][10:12])   # Tecnica
        l.append(dfTxtCont['col'][r][12:14])   # Periodo 04=Datos Diarios
        l.append(dfTxtCont['col'][r][14:16])   # Año
        l.append(dfTxtCont['col'][r][16:18])   # Mes
        for i in range(18,len(dfTxtCont['col'][r]),6): # Diferentes dias
            l.append(dfTxtCont['col'][r][i:i+5] + "  ") #quito la unidad de medida
        for j in range(len(l),37,1):        # Relleno con NaN los que tengan menos de 31
            l.append(np.nan)
        indice = len(dfContaminacion.index)
        dfContaminacion.loc[indice]=l
    return dfContaminacion

def showGraficaCont(dfContaminacion,codEstacion,codMag,act):
    
    #estPlzEspana = dfContaminacion['Estacion'] == '28079004'
    estacion = dfContaminacion['Estacion'] == codEstacion
    mag = dfContaminacion['Magnitud'] == codMag
    if act==True:
        mag = dfContaminacion['Magnitud'] == int(codMag)
    """
    arrDias = ["Dia1","Dia2","Dia3","Dia4","Dia5","Dia6","Dia7","Dia8","Dia9","Dia10","Dia11","Dia12","Dia13","Dia14","Dia15","Dia16","Dia17","Dia18","Dia19","Dia20","Dia21","Dia22","Dia23","Dia24","Dia25","Dia26","Dia27","Dia28","Dia29","Dia30","Dia31"]
    dfDias = pandas.DataFrame(columns = arrDias)
    listaDias = []
    for Dia in arrDias:
        serDia = dfContaminacion[Dia][(estacion) & mag]
        li = list(serDia)
        #lf = lf + li
        listaDias.append(li)"""
    serDia1 = dfContaminacion["Dia1"][(estacion) & mag] #Me quedo con la columna del dia 1
    serDia2 = dfContaminacion["Dia2"][(estacion) & mag] #Me quedo con la columna del dia 2
    serDia3 = dfContaminacion["Dia3"][(estacion) & mag] #...
    serDia4 = dfContaminacion["Dia4"][(estacion) & mag]
    serDia5 = dfContaminacion["Dia5"][(estacion) & mag]
    serDia6 = dfContaminacion["Dia6"][(estacion) & mag]
    serDia7 = dfContaminacion["Dia7"][(estacion) & mag]
    serDia8 = dfContaminacion["Dia8"][(estacion) & mag]
    serDia9 = dfContaminacion["Dia9"][(estacion) & mag]
    serDia10 = dfContaminacion["Dia10"][(estacion) & mag]
    serDia11 = dfContaminacion["Dia11"][(estacion) & mag]
    serDia12 = dfContaminacion["Dia12"][(estacion) & mag]
    serDia13 = dfContaminacion["Dia13"][(estacion) & mag]
    serDia14 = dfContaminacion["Dia14"][(estacion) & mag]
    serDia15 = dfContaminacion["Dia15"][(estacion) & mag]
    serDia16 = dfContaminacion["Dia16"][(estacion) & mag]
    serDia17 = dfContaminacion["Dia17"][(estacion) & mag]
    serDia18 = dfContaminacion["Dia18"][(estacion) & mag]
    serDia19 = dfContaminacion["Dia19"][(estacion) & mag]
    serDia20 = dfContaminacion["Dia20"][(estacion) & mag]
    serDia21 = dfContaminacion["Dia21"][(estacion) & mag]
    serDia22 = dfContaminacion["Dia22"][(estacion) & mag]
    serDia23 = dfContaminacion["Dia23"][(estacion) & mag]
    serDia24 = dfContaminacion["Dia24"][(estacion) & mag]
    serDia25 = dfContaminacion["Dia25"][(estacion) & mag]
    serDia26 = dfContaminacion["Dia26"][(estacion) & mag]
    serDia27 = dfContaminacion["Dia27"][(estacion) & mag]
    serDia28 = dfContaminacion["Dia28"][(estacion) & mag]
    serDia29 = dfContaminacion["Dia29"][(estacion) & mag]
    serDia30 = dfContaminacion["Dia30"][(estacion) & mag]
    serDia31 = dfContaminacion["Dia31"][(estacion) & mag]
    l1 = list(serDia1) # Paso los valores a una lista para tener el valor del dia 1 de cada mes
    l2 = list(serDia2)
    l3 = list(serDia3)
    l4 = list(serDia4)
    l5 = list(serDia5)
    l6 = list(serDia6)
    l7 = list(serDia7)
    l8 = list(serDia8)
    l9 = list(serDia9)
    l10 = list(serDia10)
    l11 = list(serDia11)
    l12 = list(serDia12)
    l13 = list(serDia13)
    l14 = list(serDia14)
    l15 = list(serDia15)
    l16 = list(serDia16)
    l17 = list(serDia17)
    l18 = list(serDia18)
    l19 = list(serDia19)
    l20 = list(serDia20)
    l21 = list(serDia21)
    l22 = list(serDia22)
    l23 = list(serDia23)
    l24 = list(serDia24)
    l25 = list(serDia25)
    l26 = list(serDia26)
    l27 = list(serDia27)
    l28 = list(serDia28)
    l29 = list(serDia29)
    l30 = list(serDia30)
    l31 = list(serDia31)
    liZip = list(zip(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31))
    lf = []
    for i in liZip:
        for j in i:
            if (float(j)>0):
                lf.append(float(j))
    """
    plt.xlabel("día del año")
    plt.ylabel("cantidad")
    nomEstacion = {
            "28079035": "Pza. del Carmen",
            "28079004": "Pza. de España",
            "28079039": "Barrio del Pilar",
            "28079008": "Escuelas Aguirre",
            "28079038": "Cuatro Caminos",
            "28079011": "Av. Ramón y Cajal",
            "28079040": "Vallecas",
            "28079016": "Arturo Soria",
            }
    nomMagnitud = {
            "01": "Dióxido de Azufre",
            "06": "Monóxido de Carbono",
            "07": "Monóxido de Nitrógeno",
            "08": "Dióxido de Nitrógeno",
            "09": "Partículas < 2.5",
            "10": "Partículas < 10",
            1: "Dióxido de Azufre",
            6: "Monóxido de Carbono",
            7: "Monóxido de Nitrógeno",
            8: "Dióxido de Nitrógeno",
            9: "Partículas < 2.5",
            "10": "Partículas < 10",
            "12": "Óxidos de Nitrógeno",
            "14": "Ozono"+" en ",
            "20": "Tolueno"+" en ",
            "30": "Benceno"+" en ",
            "35": "Etilbenceno",
            "37": "Metaxileno",
            "38": "Paraxileno",
            "39": "Ortoxileno",
            "42": "Hidrocarburos totales (hexano)",
            "43": "Metano"+" en ",
            "44": "Hidrocarburos no metánicos (hexano)",
            }
    tit = {
            "01": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "06": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "07": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "08": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "09": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "10": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "12": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "14": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "20": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "30": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "35": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "37": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "38": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "39": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "42": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "43": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            "44": nomMagnitud[codMag]+" en "+nomEstacion[codEstacion],
            }
    plt.title(tit[codMag])
    plt.plot(lf)
    plt.show()
    """
    return lf
    
def showGrafica(dirArchivo):
    dfContaminacion = pandas.DataFrame(columns = ["Estacion","Magnitud","Tecnica","Periodo_Analisis","Año","Mes","Dia1","Dia2","Dia3","Dia4","Dia5","Dia6","Dia7","Dia8","Dia9","Dia10","Dia11","Dia12","Dia13","Dia14","Dia15","Dia16","Dia17","Dia18","Dia19","Dia20","Dia21","Dia22","Dia23","Dia24","Dia25","Dia26","Dia27","Dia28","Dia29","Dia30","Dia31"])
    dfTxtCont = pandas.read_csv("datos/201709_DatosDiariosCalidadAire.txt",names=['col'])
    for r in range (0,len(dfTxtCont.index.values),1):
    #for r in range (0,10,1):
        l = []
        l.append(dfTxtCont['col'][r][0:8])     # Estacion
        l.append(dfTxtCont['col'][r][8:10])    # Magnitud
        l.append(dfTxtCont['col'][r][10:12])   # Tecnica
        l.append(dfTxtCont['col'][r][12:14])   # Periodo 04=Datos Diarios
        l.append(dfTxtCont['col'][r][14:16])   # Año
        l.append(dfTxtCont['col'][r][16:18])   # Mes
        for i in range(18,len(dfTxtCont['col'][r]),6): # Diferentes dias
            l.append(dfTxtCont['col'][r][i:i+5] + "  ") #quito la unidad de medida
        for j in range(len(l),37,1):        # Relleno con NaN los que tengan menos de 31
            l.append(np.nan)
        indice = len(dfContaminacion.index)
        dfContaminacion.loc[indice]=l
    print ("========================== CALIDAD DEL AIRE ==========================")
    estPlzCarmen = dfContaminacion['Estacion'] == '28079035'
    estPlzEspana = dfContaminacion['Estacion'] == '28079004'
    estBarrPilar = dfContaminacion['Estacion'] == '28079005'
    mag = dfContaminacion['Magnitud'] == '08'
    #print (dfContaminacion[(estPlzCarmen | estPlzEspana) & mag]["Dia1"])
    dfDias = pandas.DataFrame(columns = ["Dia1","Dia2","Dia3","Dia4","Dia5","Dia6","Dia7","Dia8","Dia9","Dia10","Dia11","Dia12","Dia13","Dia14","Dia15","Dia16","Dia17","Dia18","Dia19","Dia20","Dia21","Dia22","Dia23","Dia24","Dia25","Dia26","Dia27","Dia28","Dia29","Dia30","Dia31"])
    #serDia1 = dfContaminacion["Dia1"][(estPlzCarmen | estPlzEspana) & mag]
    serDia1 = dfContaminacion["Dia1"][(estPlzEspana) & mag]
    serDia2 = dfContaminacion["Dia2"][(estPlzEspana) & mag]
    serDia3 = dfContaminacion["Dia3"][(estPlzEspana) & mag]
    serDia4 = dfContaminacion["Dia4"][(estPlzEspana) & mag]
    serDia5 = dfContaminacion["Dia5"][(estPlzEspana) & mag]
    serDia6 = dfContaminacion["Dia6"][(estPlzEspana) & mag]
    serDia7 = dfContaminacion["Dia7"][(estPlzEspana) & mag]
    serDia8 = dfContaminacion["Dia8"][(estPlzEspana) & mag]
    serDia9 = dfContaminacion["Dia9"][(estPlzEspana) & mag]
    serDia10 = dfContaminacion["Dia10"][(estPlzEspana) & mag]
    serDia11 = dfContaminacion["Dia11"][(estPlzEspana) & mag]
    serDia12 = dfContaminacion["Dia12"][(estPlzEspana) & mag]
    serDia13 = dfContaminacion["Dia13"][(estPlzEspana) & mag]
    serDia14 = dfContaminacion["Dia14"][(estPlzEspana) & mag]
    serDia15 = dfContaminacion["Dia15"][(estPlzEspana) & mag]
    serDia16 = dfContaminacion["Dia16"][(estPlzEspana) & mag]
    serDia17 = dfContaminacion["Dia17"][(estPlzEspana) & mag]
    serDia18 = dfContaminacion["Dia18"][(estPlzEspana) & mag]
    serDia19 = dfContaminacion["Dia19"][(estPlzEspana) & mag]
    serDia20 = dfContaminacion["Dia20"][(estPlzEspana) & mag]
    serDia21 = dfContaminacion["Dia21"][(estPlzEspana) & mag]
    serDia22 = dfContaminacion["Dia22"][(estPlzEspana) & mag]
    serDia23 = dfContaminacion["Dia23"][(estPlzEspana) & mag]
    serDia24 = dfContaminacion["Dia24"][(estPlzEspana) & mag]
    serDia25 = dfContaminacion["Dia25"][(estPlzEspana) & mag]
    serDia26 = dfContaminacion["Dia26"][(estPlzEspana) & mag]
    serDia27 = dfContaminacion["Dia27"][(estPlzEspana) & mag]
    serDia28 = dfContaminacion["Dia28"][(estPlzEspana) & mag]
    serDia29 = dfContaminacion["Dia29"][(estPlzEspana) & mag]
    serDia30 = dfContaminacion["Dia30"][(estPlzEspana) & mag]
    serDia31 = dfContaminacion["Dia31"][(estPlzEspana) & mag]
    #serApp = serDia1.append(serDia2.append(serDia3.append(serDia4.append(serDia5.append(serDia6.append(serDia7.append(serDia8.append(serDia9.append(serDia10.append(serDia11))))))))))
    #serZip = (serDia1,serDia2,serDia3,serDia4,serDia5,serDia6,serDia7,serDia8,serDia9,serDia10,serDia11,serDia12,serDia13,serDia14,serDia15,serDia16,serDia17,serDia18,serDia19,serDia20)
    #serZip = zip(serDia1,serDia2)
    l1 = list(serDia1)
    l2 = list(serDia2)
    l3 = list(serDia3)
    l4 = list(serDia4)
    l5 = list(serDia5)
    l6 = list(serDia6)
    l7 = list(serDia7)
    l8 = list(serDia8)
    l9 = list(serDia9)
    l10 = list(serDia10)
    l11 = list(serDia11)
    l12 = list(serDia12)
    l13 = list(serDia13)
    l14 = list(serDia14)
    l15 = list(serDia15)
    l16 = list(serDia16)
    l17 = list(serDia17)
    l18 = list(serDia18)
    l19 = list(serDia19)
    l20 = list(serDia20)
    l21 = list(serDia21)
    l22 = list(serDia22)
    l23 = list(serDia23)
    l24 = list(serDia24)
    l25 = list(serDia25)
    l26 = list(serDia26)
    l27 = list(serDia27)
    l28 = list(serDia28)
    l29 = list(serDia29)
    l30 = list(serDia30)
    l31 = list(serDia31)
    liZip = list(zip(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31))
    lf = []
    for i in liZip:
        for j in i:
            if (float(j)>0):
                lf.append(float(j))
    #print(serApp["0"])
    #plt.plot(serApp.values)
    #plt.plot(list(liZip))
    plt.xlabel("día del año")
    plt.ylabel("cantidad")
    #plt.title("Dioxido de azufre en Plaza España")
    #plt.title("Monoxido de carbono en Plaza España")
    #plt.title("Monoxido de nitrógeno en Plaza España")
    plt.title("Dióxido de nitrógeno en Plaza España")
    plt.plot(lf)
    plt.show()
    return True
#print (dfContaminacion["Magnitud"])
