"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    Dt,Fila=[],[0, 0, 0, '']
    with open('clusters_report.txt') as Archivo:
        Rows=Archivo.readlines()
    Rows=Rows[4:]
    for i in Rows:
        if re.match('^ +[0-9]+ +', i):
            N_cluster,N_Palabras,Porcentaje,Principal=i.split()
            Fila[0]=int(N_cluster)
            Fila[1]=int(N_Palabras)
            Fila[2]=float(Porcentaje.replace(',','.')) 
            Principal.pop(0) 
            Principal=' '.join(Principal)
            Fila[3]+=Principal
        elif re.match('^\n', i) or re.match('^ +$', i):
            Fila[3] = Fila[3].replace('.', '') 
            Dt.append(Fila)
            Fila=[0, 0, 0, '']
        elif re.match('^ +[a-z]', i):
            Principal=i.split()
            Principal=' '.join(Principal)
            Fila[3]+=' '+Principal 
    df=pd.DataFrame (Dt, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df

