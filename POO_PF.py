

class Calculadora_Prestamos:
    
    def __init__(self):
        self.monto = 0
        self.tasa_mensual = 0
        self.plazo = 0
        self.cuota = 0
        
        self.tabla = []
        

   #def Cuota_mensual(self):
            
    def Entrada_data(self,p_monto,p_tasa,p_plazo):
        self.monto = p_monto
        self.tasa_mensual = ((p_tasa/12)/100)
        self.plazo = p_plazo
        
        self.cuota = round( ((self.monto * self.tasa_mensual) / (1 - (1+self.tasa_mensual)**-self.plazo)) ,2)
   
    def ver(self):
        print('CUota de ',self.cuota)
        print(self.tasa_mensual)
        print(self.tabla)


    def General_tabla(self):
        #'Pago: {0} | NULL{1} |Saldo Iniciar | CUOTA: {2} | Capital: {3} | Interes: {4} | Balance: {5}'
        last_index = 0
        
        for x in range(1,(self.plazo+1),1):
            
            #Para resolver el error logico de indexacion   
             
            if(x == 1):
                saldo_inicial = self.monto 
                intereses = (saldo_inicial*self.tasa_mensual)
                capital =  (self.cuota - intereses) 
                saldo_final = saldo_inicial - capital
                
                self.tabla.append([x,'NULL',saldo_inicial,self.cuota,capital,intereses,saldo_final])
                
            else:
                saldo_inicial = round(self.tabla[-1][6],2) 
                intereses = round((saldo_inicial*self.tasa_mensual),2) 
                capital =  round((self.cuota - intereses),2)  
                saldo_final = round(saldo_inicial - capital,2)
                
                self.tabla.append([x,'NULL',saldo_inicial,self.cuota,capital,intereses,saldo_final])         
                
#intereses = ()
#capital =  (cuota - interes)             
            
        
    
#    def Mostrar_tabla(self):
#        for x in range(1,(n+1),1):
#            print('Pago: {0} | {1} | CUOTA: {2} | Capital: {3} | Interes: {4} | Balance: {5}'.format(tabla[0],tabla[1],tabla[2],tabla[3],tabla[4],tabla[5]))   


calculador = Calculadora_Prestamos()
calculador.Entrada_data(287000,16.95,48)
calculador.General_tabla()
calculador.ver()

