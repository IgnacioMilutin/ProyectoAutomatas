def obtener_usuarios(df):
    usuarios=set()
    for i in df['Usuario']:
        usuarios.add(i)
    usuarios=list(usuarios)
    usuarios.sort()
    return usuarios

def lista(usuarios):
    usuario_diccionario={}
    for numero,usuario in enumerate(usuarios,start=1):
        print(numero,'-------',usuario)
        usuario_diccionario[numero]=usuario
    return usuario_diccionario