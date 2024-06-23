import pandas as pd
from datetime import datetime,date,time
import re

data_df=pd.read_csv('export-2019-to-now-v4.csv')
data_df['Inicio_de_Conexión_Dia'] = pd.to_datetime(data_df['Inicio_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce').dt.date

#print(data_df.dtypes)

def filtro_fechas(fecha_inicio,fecha_fin):
    pass

def filtro_usuario(usuario):
    pass


def validacion_fecha(fecha):
    fecha_re=r"^\d{4}-\d{2}-\d{2}$"
    if re.match(fecha_re,fecha):
        try: 
            fecha=datetime.strptime(fecha,'%Y-%m-%d').date()
            return fecha
        except ValueError:
            print('fecha no valida')
            return None
    else: 
        print('fecha no valida')
        return None


def validacion_usuario(df,usuario):
    if df['Usuario'].isin([usuario]).any():
        return usuario
    else: 
        print('usuario inexistente')
        return None
    
def filtro(df,fecha_inicio,fecha_fin):
    archivo_filtrado=df[(df['Inicio_de_Conexión_Dia']>=fecha_inicio) &
            (df['Inicio_de_Conexión_Dia']<=fecha_fin) 
            ]
    print(archivo_filtrado)
    return archivo_filtrado

#usuario=input('ingrese el usuario al que desea filtrar: ')
fecha_inicio=input('ingrese la fecha desde donde se quiere analizar: ')
fecha_fin=input('ingrese la fecha hasta la cual se quiere analizar: ')

fecha_inicio=validacion_fecha(fecha_inicio)
fecha_fin=validacion_fecha(fecha_fin)
#usuario=validacion_usuario(data_df,usuario)

filtro(data_df,fecha_inicio,fecha_fin)