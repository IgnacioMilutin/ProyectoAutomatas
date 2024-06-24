import pandas as pd

def filtro_fecha_usuario(df,usuario,fecha_inicio,fecha_fin):
    df_filtrado=df[(df['Inicio_de_Conexión_Dia']>=fecha_inicio) &
            (df['Inicio_de_Conexión_Dia']<=fecha_fin) &
            (df['Usuario']==usuario)]
    print(df_filtrado)
    return df_filtrado

def cant_mac_a(df_filtrado):
    cantidad=[]
    df_filtrado['']