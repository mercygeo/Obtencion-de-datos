# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:28:49 2018

@author: Mercy Pinargote
"""

import time
from Util import UtilGetData
import pandas as pd

# Start timer
start_time = time.time()
util = UtilGetData();

#Archivo que contiene la lista de url para descargar 
df=pd.read_csv('fileList.csv')

#Se hace un for para descargar los archivos y guardarlos como el mismo tipo o descomprimirlos
for index, row in df.iterrows():
    urlFileDownload, fileName=row[1],row[2]
    if(row[3]=='zip'):
        util.getZipFileUnzip(urlFileDownload, fileName)#descarga el archivo, descomprime y guarda en el destino deseado
    else:
        util.getFile(urlFileDownload, fileName)#descarga el archivo y guarda en el destino deseado

# Show elapsed time
end_time = time.time()
#Indica cuanto tiempo se tomo en ejecutar el proceso de descarga
print ("\nelapsed time: " + \
			str(round(((end_time - start_time) / 60) , 2)) + " minutes")

