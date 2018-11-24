# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:28:49 2018

@author: Mercy
"""

import time
from Util import UtilGetData
import pandas as pd

# Start timer
start_time = time.time()
util = UtilGetData();

df=pd.read_csv('fileList.csv')

for index, row in df.iterrows():
    urlFileDownload, fileName=row[1],row[2]
    if(row[3]=='zip'):
        util.getZipFileUnzip(urlFileDownload, fileName)
    else:
        util.getFile(urlFileDownload, fileName)

# Show elapsed time
end_time = time.time()
print ("\nelapsed time: " + \
			str(round(((end_time - start_time) / 60) , 2)) + " minutes")

