from reporte import Reporte
from tabla import Tabla
import pandas as pd



def analizarDatos(anterior, actual):    
  
    
    datos = Tabla(anterior, actual)    
    
    tablaTranspuesta = datos.unirTablasXmes()       
                   
    nombre = 'MonthlyReport'       
       
    
    reporte = Reporte(tablaTranspuesta, nombre)
    reporte.analizeReport()
    
    print('Reporte OK!')

