class BodegaPrincipal:
    def __init__(self, direccion, mts2):
        self.direccion=direccion
        self.mts2=mts2
        self.stock=[]        

    def abrir_bodega(self, lista):      #pasar una lista con los valores totales de los stocks de cada producto en orden según su índice del dic productos
        self.stock.extend(lista)
        
    def recepcionar_producto(self, index, valor):       #pasamos índice del dic del producto que queremos agregar y la cantidad de unidades que se agregan
        value=int(self.stock(index-1)+valor)
        self.stock(index-1, value)
        
    def descontar_producto(self, index, valor):       #pasamos índice del dic del producto que queremos descontar y la cantidad de unidades que se agregan
        value=self.stock(index-1)-valor
        self.stock(index-1, value)

    def despachar_producto(self, sucursal, index, valor):        #funcion descontar propio stock y sumarselo a una sucursal
        self.stock
        sucursal.recepcionar_producto(self, index, valor)


class Sucursal(BodegaPrincipal):
    def despachar_producto(self, bodega, index, valor):        #funcion descontar propio stock y sumarselo a una sucursal
        self.descontar_producto(self, index, valor)
        bodega.recepcionar_producto(self, index, valor)

bodegon = BodegaPrincipal("calle falsa #123", 2500)
bodegon.abrir_bodega(lista=(1000,1000,1000,1000,1000))
print(bodegon.direccion)
telovendo = Sucursal("calle false #456", 1000)
telovendo.abrir_bodega(lista=(50,50,50,50,50))
print(telovendo.stock)
bodegon.despachar_producto(telovendo, 1, 5)
print(bodegon.stock)
print(telovendo.stock)


"""
"""




"""
#Creacion de Clientes:
Liliana= Clientes(1,"Liliana","Garmendia","liligc@gmail.com","10/02/2021", 20000)
Clara=Clientes(2,"Clara", "Campos", "clara@gmail.com", "10/01/2019", 40000)
Antonia=Clientes(3,"Antonia", "Garmendia", "anto@gmail.com", "10/01/2022", 10000)
Valentina=Clientes(4,"Valentina", "Pasten", "vale@gmail.com", "20/01/2018", 50000)
Constanza=Clientes(5,"Constanza", "Campos", "cony@gmail.com", "05/01/2020", 30000)
#Creación de un diccionario con los clientes
clientes={"1":Liliana,"2":Clara, "3":Antonia, "4":Valentina, "5":Constanza}

#Creacion de proveedores
prov1= Proveedor("72635988-7", "Danilo Mardones", "Adidas_SA", "Chile", "Juridica")
prov2= Proveedor("66359188-7", "Ricardo Gonzalez", "Foster_SA", "Chile", "Juridica")
prov3= Proveedor("75635988-8", "Vanesa Saldivar", "Phillips_sa", "Chile", "Juridica")
prov4= Proveedor("69635988-3", "Fernando Perez", "Costa", "Chile", "Juridica")
prov5= Proveedor("77635988-5", "Patricio Oliva", "Casillero del Diablo", "Chile", "Juridica")
#Creación de un diccionario con los objetos proveedores
proveedores={"1":prov1, "2":prov2, "3":prov3, "4":prov4, "5":prov5}

#Creación de instancias de Productos
zapatillas= Productos(20221, "zapatillas", "calzado", proveedores["1"].razon_social, 40, 40000,"blancas", 7600)
jeans= Productos(20222, "jeans", "vestuario",proveedores["2"].razon_social , 50, 30000, "azules",5700)
audifonos= Productos(20223, "audifonos", "electronica", proveedores["3"].razon_social,50, 30000,"negros", 5700)
chocolates= Productos(20224, "bombones de chocolate", "alimentacion", proveedores["4"].razon_social, 40, 15000,"oscuro", 2850)
vino= Productos(20225, "botella de vino 1.5L","licores", proveedores["5"].razon_social, 50, 20000, "tinto",3800)
#Creación de un diccionario con los productos
productos= {"1":zapatillas, "2":jeans, "3":audifonos, "4":chocolates, "5":vino}

#Creación de instancias de Vendedores
vendedor1= Vendedor("13420605-1", "Esteban", "Contreras", "calzado",productos["1"].nombre, 0)
vendedor2= Vendedor("19620608-2", "Francisca", "Gonzalez", "vestuario",productos["2"].nombre,  0)
vendedor3= Vendedor("15530724-7", "Santiago", "Fernandez", "electronica", productos["3"].nombre, 0)
vendedor4= Vendedor("18620708-3", "Valeria", "Salinas", "alimentacion",productos["4"].nombre,  0)
vendedor5= Vendedor("17350606-5", "Juan", "Riquelme", "licores",productos["5"].nombre,  0)
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
            print("[3] Comprar producto.")
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
                Vendedor.vender()
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
            print("[3] Mostrar proveedores")
            print("[4] Eliminar productos")
            print("[5] Volver al menu principal")
            opcion3 = int(input("Seleccione una opción: "))
            
            if opcion3==1:
                Productos.mostrar_productos()
            elif opcion3==2:
                print("Este método se trabajará en el próximo trabajo")
                break
            elif opcion3==3:
                 Proveedor.mostrar_proveedores()
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
                Vendedor.vender()
            elif opcion4==4:
                break
    elif opcion1== 4:
        print("\nMuchas gracias por su preferencia, que tenga un buen día")
        break


"""