import pandas as pd
from datetime import datetime
import re

data_df=pd.read_csv('export-2019-to-now-v4.csv')
data_df['Inicio_de_Conexión_Dia'] = pd.to_datetime(data_df['Inicio_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce')
data_df['Inicio_de_Conexión_Hora'] = pd.to_datetime(data_df['Inicio_de_Conexión_Hora'], format='%H-%M-%S', errors='coerce')
data_df['FIN_de_Conexión_Dia'] = pd.to_datetime(data_df['FIN_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce')
data_df['FIN_de_Conexión_Hora'] = pd.to_datetime(data_df['FIN_de_Conexión_Hora'], format='%H-%M-%S', errors='coerce')

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
            return print('fecha no valida')
    else: return print('fecha no valida')

def validacion_hora(hora):
    hora_re=r"^\d{2}:\d{2}:\d{2}$"
    if re.match(hora_re,hora):
        try:
            hora=datetime.strptime(hora,'%H:%M:%S').time()
            return hora
        except ValueError:
            return print('hora no valida')
    else: return print('hora no valida')

def validacion_usuario(usuario):
    pass

def filtro(usuario,fecha_inicio,hora_inicio,fecha_fin,hora_fin):
    filtro=((data_df['Inicio_de_Conexión_Dia']>=fecha_inicio) &
            (data_df['Inicio_de_Conexión_Hora']>=hora_inicio) &
            (data_df['Inicio_de_Conexión_Dia']<=fecha_fin) &
            (data_df['Inicio_de_Conexión_Hora']<=hora_fin) &
            (data_df['Usuario']==usuario))
    archivo_filtrado=data_df[filtro]
    print(archivo_filtrado)
    return archivo_filtrado

usuario=input('ingrese el usuario al que desea filtrar: ')
fecha_inicio=input('ingrese la fecha desde donde se quiere analizar: ')
hora_inicio=input('ingrese la hora desde donde se quiere analizar: ')
fecha_fin=input('ingrese la fecha hasta la cual se quiere analizar: ')
hora_fin=input('ingrese la hora hasta la cual se quiere analizar: ')

fecha_inicio=validacion_fecha(fecha_inicio)
hora_inicio=validacion_hora(hora_inicio)
fecha_fin=validacion_fecha(fecha_fin)
hora_fin=validacion_hora(hora_fin)
usuario=validacion_usuario(usuario)

filtro(usuario,fecha_inicio,hora_inicio,fecha_fin,hora_fin)