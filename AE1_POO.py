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
        print("\nEl cliente :", self.nombre, self.apellido, "tiene un saldo de $", self.__saldo)
#Metodo para mostrar Id de todos los clientes
    def mostrar_id():
        print("Los clientes registrados son los siguientes:\n")
        print('{:15}{:15}'.format("Id_cliente", "Nombre"))
        print("*"*30)
        for key in clientes:
            print('{:<15}{:<15}'.format(clientes[key].id_cliente,clientes[key].nombre))
#Metodo para mostrar los saldos de todos los clientes
    def mostrar_saldostod():
        print("Los clientes registrados son los siguientes:\n")
        print('{:15}{:15}{:15}{:15}'.format("Id_cliente", "Nombre", "Apellido", "Saldo"))
        print("*"*60)
        for key in clientes:
            print('{:<15}{:<15}{:<15}{:<15}'.format(clientes[key].id_cliente,clientes[key].nombre,clientes[key].apellido,clientes[key].__saldo))

#Creacion de Clientes:
Liliana= Clientes(1,"Liliana","Garmendia","liligc@gmail.com","10/02/2021", 20000)
Clara=Clientes(2,"Clara", "Campos", "clara@gmail.com", "10/01/2019", 40000)
Antonia=Clientes(3,"Antonia", "Garmendia", "anto@gmail.com", "10/01/2022", 10000)
Valentina=Clientes(4,"Valentina", "Pasten", "vale@gmail.com", "20/01/2018", 50000)
Constanza=Clientes(5,"Constanza", "Campos", "cony@gmail.com", "05/01/2020", 30000)
#Creación de un diccionario con los clientes
clientes={"1":Liliana,"2":Clara, "3":Antonia, "4":Valentina, "5":Constanza}

#Creación de la clase Productos con el método constructor init.
class Productos:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto=0.19):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor= proveedor
        self.stock= stock
        self.valor_neto= valor_neto
        self.__impuesto= impuesto
#Metodo para mostrar catalogo de productos
    def mostrar_productos():
        print("Los siguientes productos se encuentran en nuestro catálogo:\n")
        print('{:15}{:25}{:15}{:7}{:15}'.format("Sku", "Nombre", "Categoria", "Stock", "Valor neto"))
        print("*"*75)
        for key in productos:
            print('{:<15}{:<25}{:<15}{:<7}{:<15}'.format(productos[key].sku,productos[key].nombre,productos[key].categoria,productos[key].stock, productos[key].valor_neto))
#Creación de instancias de Productos
zapatillas= Productos(20221, "zapatillas", "calzado", "Adidas_sa", 40, 40000, 7600)
jeans= Productos(20222, "jeans", "vestuario", "foster_sa", 50, 30000, 5700)
audifonos= Productos(20223, "audifonos", "electronica", "Phillips_sa",50, 30000, 5700)
chocolates= Productos(20224, "bombones de chocolate", "alimentacion", "Lind", 40, 15000, 2850)
vino= Productos(20225, "botella de vino 1.5L","licores", "Casillero del Diablo", 50, 20000, 3800)
#Creación de un diccionario con los productos
productos= {"1":zapatillas, "2":jeans, "3":audifonos, "4":chocolates, "5":vino}

#Creación de la clase Vendedor
class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision=0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision= comision
    #Metodo para mostrar catalogo de productos
    def mostrar_vendedores():
        print("Los siguientes son los vendedores de Te lo vendo Market:\n")
        print('{:15}{:15}{:15}{:15}'.format("Run", "Nombre", "Apellido", "Sección"))
        print("*"*75)
        for key in vendedores:
            print('{:<15}{:<15}{:<15}{:<15}'.format(vendedores[key].run,vendedores[key].nombre,vendedores[key].apellido,vendedores[key].seccion))
#Creación de instancias de Vendedores
vendedor1= Vendedor("13420605-1", "Esteban", "Contreras", "calzado", 0)
vendedor2= Vendedor("19620608-2", "Francisca", "Gonzalez", "vestuario", 0)
vendedor3= Vendedor("15530724-7", "Santiago", "Fernandez", "electronica", 0)
vendedor4= Vendedor("18620708-3", "Valeria", "Salinas", "alimentacion", 0)
vendedor5= Vendedor("17350606-5", "Juan", "Riquelme", "licores", 0)
vendedores={"1":vendedor1, "2":vendedor2, "3":vendedor3, "4":vendedor4, "5":vendedor5}
#Menú para acceder a los datos del cliente
while True:
    print("\n-----Bienvenido a Te lo vendo Market-----\n")
    print("[1] Clientes.")
    print("[2] Productos")
    print("[3] Vendedores")
    print("[4] Salir")
    opcion1 = int(input("Seleccione una opción: "))        
    if opcion1== 1:
        while True:
            print("\n-----Bienvenido a Te lo vendo Market-----\n")        
            print("[1] Mostrar saldo de cliente.")
            print("[2] Agregar saldo a cliente")
            print("[3] Descontar saldo a cliente.")
            print("[4] Mostrar saldo de todos los clientes")
            print("[5] Volver al menu principal")
            opcion2 = int(input("Seleccione una opción: "))
# 1. Mostrar saldo de usuario elegido:
            if opcion2 == 1:
                Clientes.mostrar_id()
                cliente_consultar= input("Seleccione un cliente del 1 al 5 que quiere ver su saldo: ")
                clientes[cliente_consultar].mostrar_saldo()
# 2. Agregar saldo a usuario elegido:
            elif opcion2 == 2:
                cliente_consultar= input("Seleccione un cliente del 1 al 5 que quiere ver su saldo: ")
                saldo= int(input("Escriba el monto que quiere agregar: "))
                clientes[cliente_consultar].agregar_saldo(saldo)
# 3. Descontar saldo a usuario elegido
            elif opcion2 == 3:
                cliente_consultar= input("Seleccione un cliente del 1 al 5 que quiere ver su saldo: ")
                saldo= int(input("Escriba el monto que quiere descontar: "))
                clientes[cliente_consultar].sacar_saldo(saldo)
#4. Mostrar todos los saldos de los clientes
            elif opcion2 == 4:
                Clientes.mostrar_saldostod()
#5. Salir de la aplicación
            elif opcion2 == 5:
                break
#Menú de acceso al catálogo de productos:
    elif opcion1== 2:
        while True:
            print("\n-----Bienvenido al catálogo de productos de Te lo vendo Market-----\n")        
            print("[1] Mostrar catálogo de productos.")
            print("[2] Modificar stock de productos")
            print("[3] Modificar precio de productos")
            print("[4] Eliminar productos")
            print("[5] Volver al menu principal")
            opcion3 = int(input("Seleccione una opción: "))
            
            if opcion3==1:
                Productos.mostrar_productos()
            elif opcion3==2:
                print("Este método se trabajará en el próximo trabajo")
                break
            elif opcion3==3:
                print("Este método se trabajará en el próximo trabajo")
                break
            elif opcion3==4:
                print("Este método se trabajará en el próximo trabajo")
                break
            elif opcion3==5:
                break
    elif opcion1== 3:
        while True:
            print("\n-----Bienvenido al area de ventas de Te lo vendo Market-----\n")        
            print("[1] Mostrar vendedores.")
            print("[2] Mostrar comision por vendedor")
            print("[3] Vender productos")
            print("[4] Volver al menu principal")
            opcion4 = int(input("Seleccione una opción: "))

            if opcion4==1:
                Vendedor.mostrar_vendedores()
            elif opcion4==2:
                print("Este método se trabajará en el próximo trabajo")
                break
            elif opcion4==3:
                print("Este método se trabajará en el próximo trabajo")
                break
            elif opcion4==4:
                break
    elif opcion1== 4:
        print("\nMuchas gracias por su preferencia, que tenga un buen día")
        break



