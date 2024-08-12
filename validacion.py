from datetime import datetime 
import re
import pandas as pd

def validacion_fecha(fecha):
    while True:
        fecha_re=r"^\d{2}-\d{2}-\d{4}$"
        if re.match(fecha_re,fecha):
            try: 
                fecha=datetime.strptime(fecha,'%d-%m-%Y').date()
                return fecha
            except ValueError:
                print('fecha no valida, ingrese la fecha con el format dd-mm-YYYY')
                return None
        else: 
            print('fecha no valida, ingrese la fecha con el format dd-mm-YYYY')
            return None

def validacion_usuario(df,numero,numero_usuario):
    usuario=numero_usuario.get(numero)
    if usuario is None:
        print('El numero ingresado no estas en lista')
        return None
    if df['Usuario'].isin([usuario]).any():
        return usuario
    else: 
        print('usuario inexistente')
        return None