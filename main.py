import pandas as pd
from datetime import datetime,date,time
from filtro import filtro_fecha_usuario, cant_mac_a
from validacion import validacion_usuario,validacion_fecha
from to_excel import to_excel
from lista_usuarios import lista,obtener_usuarios
import threading

data_df=pd.read_csv('export-2019-to-now-v4.csv')

data_df['Inicio_de_Conexión_Dia'] = pd.to_datetime(data_df['Inicio_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce').dt.date
data_df['Usuario']=data_df['Usuario'].astype(str)

def main():
    stop='Y'
    while stop=='Y':
        #proceso_interfaz = threading.Thread(target=app, args=(data_df,))
        #proceso_interfaz.stasrt()
        usuarios=obtener_usuarios(data_df)
        usuario_diccionario=lista(usuarios)
        usuario=None
        while usuario is None:
            numero=int(input('ingrese el numero correspondiente al usuario que desea filtrar: '))
            usuario=validacion_usuario(data_df,numero,usuario_diccionario)
        fecha_inicio=None
        while fecha_inicio is None:
            fecha_inicio=input('ingrese la fecha desde donde se quiere analizar (DD-MM-YYYY): ')
            fecha_inicio=validacion_fecha(fecha_inicio)
        fecha_fin=None
        while fecha_fin is None:
            fecha_fin=input('ingrese la fecha hasta la cual se quiere analizar (DD-MM-YYYY): ')
            fecha_fin=validacion_fecha(fecha_fin)
        df_filtrado=filtro_fecha_usuario(data_df,usuario,fecha_inicio,fecha_fin)
        cant_mac_a(df_filtrado)
        print(df_filtrado)
        while True:
            confirmacion=input('Desea descargar el archivo filtrado? (Y/n): ').upper()
            if confirmacion=='Y':
                break
            elif confirmacion=='N':
                break
            else: print('entrada no valida, ingrese Y o n')
        to_excel(df_filtrado,confirmacion)
        while True:
            stop=input('Desea volver a ejecutar el programa? (Y/n): ').upper()
            if stop=='Y':
                break
            elif stop=='N':
                break
            else: print('entrada no valida, ingrese Y o n')
    return print('Gracias por utilizar el programa')

main()