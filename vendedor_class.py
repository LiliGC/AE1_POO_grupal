class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision=0, empleado_de_mes=0): # empleado del mes es el argumento opcional del abp2
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision=comision
        self.empleado_del_mes=empleado_de_mes

    def setComision(self,venta):
        self.__comision+=venta*0.05/100
        print(f"Comision por la compra realizada de {venta*0.5/100}")
        print(f"Usted lleva acumulado {self.__comision}.")
        return self.__comision

    def vender(self, prod, cli):      
        var2 = int(prod.valor_neto+(prod.valor_neto*1.19/100))
        var = int(prod.valor_neto*0.5/100)
        if prod.stock >= 1 and cli._Cliente__saldo >= var2:
            print(f"Compra Autorizada\nUsted venderá 1 unidad de {prod.stock} del producto {prod.nombre}")
            prod.stock -= 1
            print(f"El nuevo stock de {prod.nombre} es de {prod.stock} unidad(es).")            
            print(f"Comision por la compra realizada de ${var}")
            self.__comision += var
            print(f"Usted lleva acumulado ${self.__comision}.")
            cli._Cliente__saldo -= var2 #se hace el descuento del saldo
        else: 
            print("Compra Rechazada")


        """
    #Metodo para mostrar vendedores
    def mostrar_vendedores():       #PROBABLY WILL NOT WORK
        print("Los siguientes son los vendedores de Te lo vendo Market:\n")
        print('{:15}{:15}{:15}{:15}{:15}'.format("Run", "Nombre", "Apellido", "Sección", "Comision"))
        print("*"*75)
        for key in vendedores:
            print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(vendedores[key].run,vendedores[key].nombre,vendedores[key].apellido,vendedores[key].seccion, vendedores[key].__comision))

"""
