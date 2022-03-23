class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision=0): # compra será para ingresar objeto producto a comprar
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision=comision


    def setComision(self,venta):
        self.__comision+=venta*0.05/100
        print(f"Comision por la compra realizada de {venta*0.05/100}")
        print(f"Usted lleva acumulado {self.__comision}.")
        return self.__comision

        
    #Metodo para mostrar vendedores
    def mostrar_vendedores():       #PROBABLY WILL NOT WORK
        print("Los siguientes son los vendedores de Te lo vendo Market:\n")
        print('{:15}{:15}{:15}{:15}{:15}'.format("Run", "Nombre", "Apellido", "Sección", "Comision"))
        print("*"*75)
        for key in vendedores:
            print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(vendedores[key].run,vendedores[key].nombre,vendedores[key].apellido,vendedores[key].seccion, vendedores[key].__comision))




    def vender(self, prod, cli):       #CAMBIAR
        if prod.stock >= 1:
            print(f"Compra Autorizada\nUsted venderá 1 unidad de {prod.stock} del producto {prod.nombre}")
            prod.stock -= 1
            print(f"El nuevo stock de {prod.nombre} es de {prod.stock} unidad(es).")
            def setCo
            print(f"Comision por la compra realizada de {self.aux}")
            print(f"Usted lleva acumulado {self.__comision}.")            
            return [self.compra.stock, self.__comision]
        else: 
            print("Compra Rechazada")

