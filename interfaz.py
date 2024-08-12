import tkinter as tk
import pandas as pd

def obtener_usuarios(df):
    usuarios=set()
    for i in df['Usuario']:
        usuarios.add(i)
    list(usuarios)
    return usuarios

def mostrar_usuarios(df,text_usuarios):
    usuarios_unicos = obtener_usuarios(df)
    text_usuarios.delete(1.0, tk.END)
    for usuario in usuarios_unicos:
        text_usuarios.insert(tk.END, usuario + "\n")

def app(df):
    global text_usuarios
    app = tk.Tk()
    app.title("Lista de Usuarios")
    text_usuarios = tk.Text(app, height=50, width=50)
    btn_mostrar = tk.Label(app, command=mostrar_usuarios(df,text_usuarios))
    text_usuarios.pack(padx=10, pady=10)
    btn_mostrar.pack()
    app.mainloop()