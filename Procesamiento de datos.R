library(haven) #para leer archivos spss
library(reshape2)#para hacer transformaciones en los dataframes
library(sqldf)#para ejecutar sentencias SQL
Defunciones_2000_2016 <- read.delim2("C:/MERCY UOC/Segundo Semestre/Periodismo de datos/PEC3/Descargas/Defunciones_2000_2016.txt")
summary(Defunciones_2000_2016)
Defunciones_2000_2016_genero <- read.delim("C:/MERCY UOC/Segundo Semestre/Periodismo de datos/PEC3/Descargas/Defunciones_2000_2016_genero.txt", encoding="utf8towcs")
summary(Defunciones_2000_2016_genero)