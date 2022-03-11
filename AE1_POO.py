#Creacion de las clases Clientes, Productos y Vendedor:
#Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo. 
# Como se encuentra trabajando en el desarrollo del módulo de Python Básico, 
# se solicita integrar correctamente los métodos de las clases en las opciones del menú desarrollado. 
# Desarrollar 5 instancias de cada clase creada en los puntos anteriores. 
# Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o gráfica. 
# Desarrollen el ejercicio de forma intuitiva.

class Clientes:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_de_registro, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo= correo
        self.fecha_de_registro= fecha_de_registro
        self.__saldo= saldo
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
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto=1.19 ):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor= proveedor
        self.stock= stock
        self.valor_neto= valor_neto
        self.__impuesto= impuesto

class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision=0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision= comision
