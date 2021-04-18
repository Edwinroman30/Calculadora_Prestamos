from tabulate import tabulate
from datetime import timedelta,datetime

class Calculadora_Prestamos:
    
    def __init__(self):
        self.monto = 0
        self.tasa_mensual = 0
        self.plazo = 0
        self.cuota = 0
        
        self.tabla_amortizacion = []
        
            
    def Entrada_data(self):
        #TOMAR ESTE PUNTO EN CUENTA PARA HACER LA ENTRADA POR TECLADO.
        self.monto = float(input('Monto del prestamo en RD$: '))
        #converTasa = ((float(input('Monto del prestamo en RD$: '))/12)/100)
        self.tasa_mensual = ((float(input('Tasa de Porcentaje Anual: '))/12)/100)
        self.plazo = int(input('Plazo en meses: '))
        
        self.cuota = round( ((self.monto * self.tasa_mensual) / (1 - (1+self.tasa_mensual)**-self.plazo)) ,2)
   
    
    #Muestra la tabla_amortizacion
    def Mostrar_tabla_amortizacion(self):
        print(tabulate(self.tabla_amortizacion, floatfmt='.2f',headers=["Pago","Fecha Pago","Saldo Iniciar","Cuota","Capital","Interes","Balance"], tablefmt='fancy_grid'))

    
    #Metodo nucleo que me permite general los calculos.
    def General_tabla_amortizacion(self):
        
        #Para poder trabajar con la fecha.
        formato_fecha = "%d-%b-%Y"
        fecha_prestamo = datetime.now()


        for x in range(1,(self.plazo+1),1):
            
            #Por cada ciclo sumo un mes a la fecha actuar.
            fecha_prestamo = fecha_prestamo + timedelta(days=+30)
                          
            if(x == 1):
                saldo_inicial = round(self.monto,2) 
                intereses = round((saldo_inicial*self.tasa_mensual),2) 
                capital =  round((self.cuota - intereses) ,2) 
                saldo_final = round(saldo_inicial - capital,2) 
                
                self.tabla_amortizacion.append([x,fecha_prestamo.strftime(formato_fecha),saldo_inicial,self.cuota,capital,intereses,saldo_final])
                
            else:
                saldo_inicial = round(self.tabla_amortizacion[-1][6],2) 
                intereses = round((saldo_inicial*self.tasa_mensual),2) 
                capital =  round((self.cuota - intereses),2)  
                saldo_final = round(saldo_inicial - capital,2)
                
                self.tabla_amortizacion.append([x, fecha_prestamo.strftime(formato_fecha) ,saldo_inicial,self.cuota,capital,intereses,saldo_final])         
                #FORMATO DE INSERCION EN LA TABLA => 'Pago: {0} | Fecha |Saldo Iniciar | CUOTA: {2} | Capital: {3} | Interes: {4} | Balance o Saldo Final: {5}'
                   
    
  


#INSTANCIANDO LA CLASE
calculador = Calculadora_Prestamos()
calculador.Entrada_data()
calculador.General_tabla_amortizacion()
calculador.Mostrar_tabla_amortizacion()
