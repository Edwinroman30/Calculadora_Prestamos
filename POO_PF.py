#MODULOS A USAR:
from tabulate import tabulate
from datetime import timedelta,datetime

class Calculadora_Prestamos:
    
    def __init__(self):
        self.monto = 0
        self.tasa_mensual = 0
        self.plazo = 0
        self.cuota = 0
        
        self.tabla_amortizacion = []
        
        print('Edwin Dev Presenta: Calculadora de Prestamos \n')
        
    #El método [Entrada_data] es super importante porque permite ingresar los datos esenciales.        
    def Entrada_data(self):
        self.monto = float(input('Monto del prestamo en RD$: '))
        
        #*En este proceso se convierte directamente la tasa de anual a tasa mensual. Y también se termina de convertir en porcentuaje.
        self.tasa_mensual = ((float(input('Tasa de Porcentaje Anual: '))/12)/100)
        
        self.plazo = int(input('Plazo en meses: '))
        
        #Aquí simplemente con los datos anteriormente recolectados se esta CALCULANDO LA CUOTA.
        self.cuota = round( ((self.monto * self.tasa_mensual) / (1 - (1+self.tasa_mensual)**-self.plazo)) ,2)
   
    
    #El método [Mostrar_tabla_amortizacion] muestra la tabla_amortizacion usando TABULATE.
    def Mostrar_tabla_amortizacion(self):
        print(tabulate(self.tabla_amortizacion, floatfmt='.2f',headers=["Pago","Fecha Pago","Saldo Iniciar","Cuota","Capital","Interes","Balance"], tablefmt='fancy_grid'))

    
    #El método [General_tabla_amortizacion] es el nucleo que me permite general los cálculos.
    def General_tabla_amortizacion(self):
        
        #Para poder trabajar con la fecha.
        formato_fecha = "%d-%b-%Y"
        fecha_prestamo = datetime.now()

        #Esto se repetirá según el PLAZO. 
        for x in range(1,(self.plazo+1),1):
            
            #Por cada ciclo sumo un mes a la fecha actuar.
            fecha_prestamo = fecha_prestamo + timedelta(days=+30)
                          
            if(x == 1):
                saldo_inicial = round(self.monto,2) 
                intereses = round((saldo_inicial*self.tasa_mensual),2) 
                capital =  round((self.cuota - intereses) ,2) 
                saldo_final = round(saldo_inicial - capital,2) 
                
                #Orden de inserción: [Num_pago, fecha_prestamo, saldo inicial generado, cuota, capital generado, interes generado, saldo final o balance generado]
                self.tabla_amortizacion.append([x,fecha_prestamo.strftime(formato_fecha),saldo_inicial,self.cuota,capital,intereses,saldo_final])
                
            else:
                saldo_inicial = round(self.tabla_amortizacion[-1][6],2) 
                intereses = round((saldo_inicial*self.tasa_mensual),2) 
                capital =  round((self.cuota - intereses),2)  
                saldo_final = round(saldo_inicial - capital,2)
                
                self.tabla_amortizacion.append([x, fecha_prestamo.strftime(formato_fecha) ,saldo_inicial,self.cuota,capital,intereses,saldo_final])         
                #FORMATO DE INSERCION EN LA TABLA => 'Pago: {0} | Fecha |Saldo Iniciar | CUOTA: {2} | Capital: {3} | Interes: {4} | Balance o Saldo Final: {5}'
                   
    
  

#INSTANCIANDO LA CLASE:

calculador = Calculadora_Prestamos() #DENIENDO EL OBJETO

calculador.Entrada_data() #ENTRADA DE DATOS
calculador.General_tabla_amortizacion() #PROCESO QUE HACE LOS CALCULOS
calculador.Mostrar_tabla_amortizacion() #MUESTRA DE LA TABLA

#Edwin Alberto Roman Seberino
#2020-10233
#Grupo o Seccion - #11
#Fundamentos de programación-2021-C-1-Miguel Liceares Moreta Rodriguez