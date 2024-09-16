import pandas as pd
from unipath import Path

def to_excel(df,confirmacion):
    if confirmacion=='Y':
        nombre=input('ingrese el nombre de su archivo, CON .xlsx AL FINAL DE NOMBRE ELEGIDO: ')
        ruta=Path(nombre)
        df.to_excel(ruta,index=True)
        if ruta.exists():
            print('Archivo creado correctamente')
        else:
            print('No se creo el archivo, pruebe nuevamente')
        return None
    elif confirmacion=='N':
        print('No se creo el archivo')
        return None
    else: 
        print('Entrada no valida')
        return None