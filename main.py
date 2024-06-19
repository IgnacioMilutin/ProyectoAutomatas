import pandas as pd

data_df=pd.read_csv('export-2019-to-now-v4.csv',parse_dates=True,date_format="%Y-%m-%d")
#df['Inicio_de_Conexión_Dia'] = pd.to_datetime(df['Inicio_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce') Funciona para convertir a datetime, verificar si conviene
print(data_df.dtypes)

def filtro_fechas(fecha_inicio,fecha_fin):
    pass

def filtro_usuario(usuario):
    pass

