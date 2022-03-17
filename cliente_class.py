class Cliente:

    def __init__(self, id_cliente, nombre, apellido, correo, fecha_de_registro, ubicacion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo= correo
        self.fecha_de_registro= fecha_de_registro
        self.__saldo= 0
        self.ubicacion= ubicacion


#Metodo para agregar saldo al Cliente
    def setSaldo1(self,saldo):
        self.__saldo+=saldo

#Metodo para descontar saldo al Cliente
    def setSaldo2(self, saldo):
        set.self.__saldo=self.__saldo-saldo

#Metodo para mostrar saldo
    def getSaldo(self):
        show = self.__saldo
        print(f"El cliente :, {self.nombre}, {self.apellido}, tiene un saldo de $, {show}")

cli1 = Cliente(1, "diego", "gonzalez", "asd@as.com", "23/23/21", "valparaiso")
clientes={"1":cli1}


cli1.setSaldo1(90000)
#print(cli1.nombre)
#cli1.getSaldo()
