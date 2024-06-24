import pandas as pd
from datetime import datetime,date,time
from filtro import filtro_fecha_usuario, cant_mac_a
from validacion import validacion_usuario,validacion_fecha

data_df=pd.read_csv('export-2019-to-now-v4.csv')

data_df['Inicio_de_Conexión_Dia'] = pd.to_datetime(data_df['Inicio_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce').dt.date
data_df['Usuario']=data_df['Usuario'].astype(str)
#print(data_df.dtypes)

usuario=input('ingrese el usuario al que desea filtrar: ')
fecha_inicio=input('ingrese la fecha desde donde se quiere analizar: ')
fecha_fin=input('ingrese la fecha hasta la cual se quiere analizar: ')

fecha_inicio=validacion_fecha(fecha_inicio)
fecha_fin=validacion_fecha(fecha_fin)
usuario=validacion_usuario(data_df,usuario)

df_filtrado=filtro_fecha_usuario(data_df,usuario,fecha_inicio,fecha_fin)
cant_mac_a(df_filtrado)