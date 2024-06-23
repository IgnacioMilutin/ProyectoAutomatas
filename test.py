import unittest
import pandas as pd
from datetime import datetime
from main import filtro, validacion_fecha, validacion_hora

#class TestFiltroFinal(unittest.TestCase):
 #   def setUp(self):
  #      df=pd.read_csv('test_data.csv')
   # def test_1disp(self):
    #    self.assertEqual()

test_df=pd.read_csv('test_data.csv')

test_df['Inicio_de_Conexión_Dia'] = pd.to_datetime(test_df['Inicio_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce').dt.date
test_df['Inicio_de_Conexión_Hora'] = pd.to_datetime(test_df['Inicio_de_Conexión_Hora'], format='%H-%M-%S', errors='coerce').dt.time
test_df['FIN_de_Conexión_Dia'] = pd.to_datetime(test_df['FIN_de_Conexión_Dia'], format='%Y-%m-%d', errors='coerce').dt.date
test_df['FIN_de_Conexión_Hora'] = pd.to_datetime(test_df['FIN_de_Conexión_Hora'], format='%H-%M-%S', errors='coerce').dt.time

print(test_df.dtypes)

usuario_test=input('ingrese el usuario al que desea filtrar: ')
fecha_inicio_test=input('ingrese la fecha desde donde se quiere analizar: ')
hora_inicio_test=input('ingrese la hora desde donde se quiere analizar: ')
fecha_fin_test=input('ingrese la fecha hasta la cual se quiere analizar: ')
hora_fin_test=input('ingrese la hora hasta la cual se quiere analizar: ')

fecha_inicio=validacion_fecha(fecha_inicio_test)
hora_inicio=validacion_hora(hora_inicio_test)
fecha_fin=validacion_fecha(fecha_fin_test)
hora_fin=validacion_hora(hora_fin_test)
#usuario=validacion_usuario(usuario)

filtro(test_df,usuario_test,fecha_inicio_test,hora_inicio_test,fecha_fin_test,hora_fin_test)