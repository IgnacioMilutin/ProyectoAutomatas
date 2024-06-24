import pandas as pd

def filtro_fecha_usuario(df,usuario,fecha_inicio,fecha_fin):
    df_filtrado=df[(df['Inicio_de_Conexión_Dia']>=fecha_inicio) &
            (df['Inicio_de_Conexión_Dia']<=fecha_fin) &
            (df['Usuario']==usuario)]
    return df_filtrado

def cant_mac_a(df_filtrado):
    cantidad=set()
    for i in df_filtrado['MAC_Cliente']:
        cantidad.add(i)
    list(cantidad)
    nro_cant=len(cantidad)
    print(nro_cant)
    return nro_cant