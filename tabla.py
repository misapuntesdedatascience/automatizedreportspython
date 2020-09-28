import pandas as pd


class Tabla:    
    
    def __init__(self, anterior,actual):  
        self.anterior = anterior
        self.actual = actual
       
   
    def unirTablasXmes(self):                      
        
        df1 = pd.DataFrame()
        for x in range(len(self.anterior.index)):
            mesAnterior = list(self.anterior['Barrio']) 
            mesActual = list(self.actual['Barrio']) 
            if mesAnterior[x] in mesActual:
                df1 = df1.append(self.anterior.loc[(self.anterior['Barrio'] == self.anterior['Barrio'][x])]) 
                df1 = df1.append(self.actual.loc[(self.actual['Barrio'] == self.anterior['Barrio'][x])])
                
            
        column_names = df1.columns
        
        df1 = df1.reset_index(drop=True)
       
        tablaTranspuesta = self.transponerTablas(df1)
        
        return tablaTranspuesta      
   
        
    def transponerTablas(self, tabla): 
      
       
        lista_sheets = pd.DataFrame()
        for y in range(len(tabla.index)):          
          
           
           if y == 0  or y %2 == 0:
               sheet1 = pd.DataFrame()
               sheet = pd.DataFrame()
               sheet = sheet.append(tabla.loc[tabla['Barrio'] == tabla['Barrio'][y]])                            
               
               name_columns = ['Mes anterior','Mes Actual']
                
               sheet1 = sheet.copy()
               sheet1 = sheet1.T
               sheet1.columns = name_columns                       
        
               lista_sheets = pd.concat([lista_sheets, sheet1])
       
           
          
         
                
        return lista_sheets
            
           
    