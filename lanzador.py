from utilidades import analizarDatos
import pandas as pd

mesAnterior = pd.read_excel("./raw_data/reportEne.xlsx")
mesActual = pd.read_excel("./raw_data/reportFeb.xlsx")




analizarDatos(mesAnterior, mesActual)    