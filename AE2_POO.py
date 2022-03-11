#Agregar una clase Proveedor con los siguientes atributos:
#  ● RUT ● Nombre Legal ● Razón Social ● País ● Una distinción entre persona jurídica o persona natural 
# A las clases creadas en la actividad anterior, incorpore un atributo opcional a cada una.
#  Al momento de instanciar un objeto de la clase Producto, deberá existir una Composición con la clase Proveedor. 
# Se deberá crear un método vender de la clase Vendedor y esta deberá descontar el valor del atributo stock de la clase Producto 
# y calcular un 0.5% de comisión referente al valor_neto del producto y luego sumarlo al atributo comisión de la clase Vendedor. 
# Luego el método deberá calcular el valor final del producto y descontarlo del atributo saldo de la clase Cliente. 
# Se solicita que existan condicionales para realizar validaciones correspondientes, como por ejemplo si no existe saldo suficiente en la clase Cliente, 
# este deberá mostrar un mensaje indicando que no es posible adquirir el producto por saldo insuficiente, de la misma forma para el stock de productos. Desarrolle cuatro métodos más para dinamizar la interacción entre diferentes clases e instancias. Al menos uno de estos métodos debe aplicar los contenidos de ‘sobrecarga de métodos’.
class Clientes:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_de_registro, saldo, opcional):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo= correo
        self.fecha_de_registro= fecha_de_registro
        self.__saldo= saldo
        self.opcional= opcional
#Metodo para agregar saldo al Cliente
    def agregar_saldo(self,saldo):
        self.__saldo=self.__saldo+saldo
#Metodo para descontar saldo al Cliente
    def sacar_saldo(self, saldo):
        self.__saldo=self.__saldo-saldo
#Metodo para mostrar saldo
    def mostrar_saldo(self):
        print("El cliente :", self.nombre, self.apellido, "tiene un saldo de $", self.__saldo)
#Creacion de Clientes:
Liliana= Clientes(1,"Liliana","Garmendia","liligc@gmail.com","10/02/2021", 20000)
Clara=Clientes(2,"Clara", "Campos", "clara@gmail.com", "10/01/2019", 40000)
Antonia=Clientes(3,"Antonia", "Garmendia", "anto@gmail.com", "10/01/2022", 10000)
Valentina=Clientes(4,"Valentina", "Pasten", "vale@gmail.com", "20/01/2018", 50000)
Constanza=Clientes(5,"Constanza", "Campos", "cony@gmail.com", "05/01/2020", 30000)

clientes={"1":Liliana,"2":Clara, "3":Antonia, "4":Valentina, "5":Constanza}

clientes["1"].mostrar_saldo()
print(clientes["1"].nombre)
clientes["1"].agregar_saldo(50000)
clientes["1"].mostrar_saldo()
print(Liliana.nombre)
print(Liliana.correo)
print(Liliana.fecha_de_registro)
Liliana.fecha_de_registro="20/03/2019"
print(Liliana.fecha_de_registro)
Liliana.mostrar_saldo()
Liliana.agregar_saldo(40000)
Liliana.mostrar_saldo()
Liliana.sacar_saldo(50000)
Liliana.mostrar_saldo()

class Productos:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto=1.19, opcional2):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor= proveedor
        self.stock= stock
        self.valor_neto= valor_neto
        self.__impuesto= impuesto
        self.opcional2= opcional2

class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision=0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision= comision

class Proveedor:
    def __init__(self, rut, nombre_legal, razon_social, pais, juridica):
        self.rut=rut
        self.nombre_legal= nombre_legal
        self.razon_social= razon_social
        self.pais= pais
        self.juridica= juridica
    
