import unittest
import pandas as pd
from datetime import datetime
from main import filtro, validacion_fecha, validacion_hora

#class TestFiltroFinal(unittest.TestCase):
 #   def setUp(self):
  #      df=pd.read_csv('test_data.csv')
   # def test_1disp(self):
    #    self.assertEqual()

data_df=pd.read_csv('test_data.csv')

data_df['Inicio_de_Conexión_Dia'] = pd.to_datetime(data_df['Inicio_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce').dt.date
data_df['Inicio_de_Conexión_Hora'] = pd.to_datetime(data_df['Inicio_de_Conexión_Hora'], format='%H-%M-%S', errors='coerce').dt.time
data_df['FIN_de_Conexión_Dia'] = pd.to_datetime(data_df['FIN_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce').dt.date
data_df['FIN_de_Conexión_Hora'] = pd.to_datetime(data_df['FIN_de_Conexión_Hora'], format='%H-%M-%S', errors='coerce').dt.time

print(data_df.dtypes)

usuario=input('ingrese el usuario al que desea filtrar: ')
fecha_inicio=input('ingrese la fecha desde donde se quiere analizar: ')
hora_inicio=input('ingrese la hora desde donde se quiere analizar: ')
fecha_fin=input('ingrese la fecha hasta la cual se quiere analizar: ')
hora_fin=input('ingrese la hora hasta la cual se quiere analizar: ')

fecha_inicio=validacion_fecha(fecha_inicio)
hora_inicio=validacion_hora(hora_inicio)
fecha_fin=validacion_fecha(fecha_fin)
hora_fin=validacion_hora(hora_fin)
#usuario=validacion_usuario(usuario)

filtro(usuario,fecha_inicio,hora_inicio,fecha_fin,hora_fin)