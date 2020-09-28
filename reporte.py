import pandas as pd
from datetime import date
import os

class Reporte:       
     
    def __init__(self, report, nombre): 
        self.report = report      
        self.nombre = nombre
   
    
    def analizeReport(self):
        
        today = str(date.today())
        
       # Comprobamos si el archivo ya existe, si existe lo eliminamos 
        
        if os.path.isfile('./informes/%s_%s.xlsx' % (self.nombre, today)):
            os.remove('./informes/%s_%s.xlsx' % (self.nombre, today))           
   
        excel_file = './informes/%s_%s.xlsx' % (today, self.nombre)        
        
    
        sheet_name = 'Reporte'
    
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        self.report.to_excel(writer, sheet_name=sheet_name, header = None)
    
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]    
        
        
        cell_format = workbook.add_format()      
        ajustar_texto = workbook.add_format()       
        ajustar_texto.set_text_wrap()
        
       
        ajustar_texto.set_align('center')
        izq = workbook.add_format()
        izq.set_text_wrap()
        izq.set_align('left')
       
        worksheet.freeze_panes(0,1)
        worksheet.set_default_row(20)
        worksheet.set_column('A:A', 20, cell_format)  
        worksheet.set_column('B:B', 25, ajustar_texto)
        worksheet.set_column('C:C', 25, ajustar_texto) 
        worksheet.set_column('D:D', 5, ajustar_texto)         
        worksheet.set_column('E:E', 5, ajustar_texto) 
        
    
        cantidadGimnasios =  int((len(self.report)+1)/8)         
        
            
        def formatFilaTitulo():    
            for x in range(cantidadGimnasios):                                     
             
                                   
                if x == 0:
                      filaTitulo = 0  
                      filaBarrio = 1
             
                 
                data_format = workbook.add_format({'bg_color': '#f0f9d8', 
                                                   'bold': True,
                                                   'text_wrap': True,
                                                   'align': 'center',
                                                   'valign': 'center',
                                                   'border': 3}) 

                #data_format.set_text_wrap()
                #data_format.set_align('center')
                worksheet.set_row(filaTitulo, 20, cell_format=data_format)
               
                formatBarrio = workbook.add_format()
                #cell_format.set_pattern(1)  # This is optional when using a solid fill.
                formatBarrio.set_bg_color('#f0f9d8')
                formatBarrio.set_bold()  
                formatBarrio.set_font_size(15)                                     
                formatBarrio.set_align('center')               
                
                
                worksheet.write('A%s' % (filaBarrio), 'Sede', formatBarrio)             
               
                filaTitulo += 8
                filaBarrio += 8            
              
   
        def agregarColumnaDePorcentaje():       
                        
            for x in range(cantidadGimnasios): 
               
               if x == 0:
                   filaEntregados = 2    
            
               calcularPorcentaje(filaEntregados)                   
              
               
               filaEntregados += 8
               
 
        def calcularPorcentaje(fila):
            formatoPorcentajes = workbook.add_format() 
            formatoPorcentajes.set_bold() 
            filaPorcentaje = fila+1
            
            for ratio in range(6):
               
               ratioAnterior = self.report.iloc[fila][0]                  
              
               
               
               ratioActual = self.report.iloc[fila][1]
             
               
               
               if ratioAnterior == 0 and ratioActual > 0:
                    porcentajeRatio = 100
                   
               elif ratioAnterior == 0:                   
                    porcentajeRatio = 0                    
             
               else:
                    porcentajeRatio = ((ratioActual*100)/ratioAnterior)-100
                   
                   #porcentajeRatio = float("{:.0%}".format(round((ratioActual/ratioAnterior)-1,2)))                  
                              
                            
               worksheet.write('E%s' % (filaPorcentaje), '%.i%%' % (porcentajeRatio) , formatoPorcentajes)
               if porcentajeRatio > 0:
                   worksheet.insert_image('D%s' % (filaPorcentaje), 'up.png', {'x_scale': 1, 'y_scale': 1})
               
               elif porcentajeRatio < 0:
                   worksheet.insert_image('D%s' % (filaPorcentaje), 'down.png', {'x_scale': 1, 'y_scale': 1})   
            
               else:
                   worksheet.insert_image('D%s' % (filaPorcentaje), 'equal.png', {'x_scale': 1, 'y_scale': 1})    
                   
        
                   
               
               fila += 1
               filaPorcentaje += 1
                                                           
      
        formatFilaTitulo()       
        agregarColumnaDePorcentaje()
        
        writer.save()    
        return writer 

