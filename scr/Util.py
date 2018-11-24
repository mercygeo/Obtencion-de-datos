# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:28:49 2018

@author: Mercy Pinargote
"""

import requests, io
from zipfile import ZipFile

class UtilGetData():
    def __init__(self):
        self.fileName=""
        self.urlFileDownload=""
        
    #Download files and save it in predifined folder 
    def getFile(self, urlFileDownload, fileName):    
        resp = requests.get(urlFileDownload )
        output = open(fileName, 'wb')
        output.write(resp.content)
        output.close()
    
    #Download zip files. Unzip and save it in predifined forlder
    def getZipFileUnzip(self, urlFileDownload, fileName ):        
        resp = requests.get(urlFileDownload )
        myzip = ZipFile(io.BytesIO(resp.content))
        myzip.extractall(fileName)    
        
    