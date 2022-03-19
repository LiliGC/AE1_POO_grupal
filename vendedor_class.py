class Vendedor:

    def __init__(self, run, nombre, apellido, seccion): # compra será para ingresar objeto producto a comprar
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision= 0
        self.aux = 0

    def vender(self):
        if self.compra.stock > 1:
            print(f"Compra Autorizada\nUsted venderá 1 unidad de {self.compra.stock} del producto {self.compra.nombre}")
            self.compra.stock -= 1
            print(f"El nuevo stock de {self.compra.nombre} es de {self.compra.stock} unidad(es).")
            self.aux = 0.005*(self.compra.valor_neto)
            self.__comision += self.aux
            print(f"Comision por la compra realizada de {self.aux}")
            print(f"Usted lleva acumulado {self.__comision}.")
            
            input()
            return [self.compra.stock, self.__comision]
        else: 
            print("Compra Rechazada")
            input()

