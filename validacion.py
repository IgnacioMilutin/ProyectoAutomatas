from datetime import datetime 
import re
import pandas as pd

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
        return False