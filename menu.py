from bodega_class import BodegaPrincipal, Sucursal
from proveedor_class import Proveedor
from producto_class import Producto
from cliente_class import Cliente
from vendedor_class import Vendedor

a={"1":1000,"2":1000,"3":1000, "4":1000, "5":1000}
bodega=BodegaPrincipal("Arlegui 400 Viña del Mar", 5000, a)
sucursal=Sucursal("1 Norte 1400 Viña del Mar", 1000,{"1":20,"2":20,"3":30, "4":20, "5":30} )

prov1= Proveedor("72635988-7", "Danilo Mardones", "Adidas_SA", "Chile", "Juridica")
prov2= Proveedor("66359188-7", "Ricardo Gonzalez", "Foster_SA", "Chile", "Juridica")
prov3= Proveedor("75635988-8", "Vanesa Saldivar", "Phillips_sa", "Chile", "Juridica")
prov4= Proveedor("69635988-3", "Fernando Perez", "Costa", "Chile", "Juridica")
prov5= Proveedor("77635988-5", "Patricio Oliva", "Casillero del Diablo", "Chile", "Juridica")
#Creación de un diccionario con los objetos proveedores
proveedores={"1":prov1, "2":prov2, "3":prov3, "4":prov4, "5":prov5}

zapatillas= Producto(20221, "zapatillas", "calzado", proveedores["1"].razon_social, sucursal.stock["1"], 40000,"blancas")
jeans= Producto(20222, "jeans", "vestuario",proveedores["2"].razon_social , sucursal.stock["2"], 30000, "azules")
audifonos= Producto(20223, "audifonos", "electronica", proveedores["3"].razon_social,sucursal.stock["3"], 30000,"negros")
chocolates= Producto(20224, "bombones de chocolate", "alimentacion", proveedores["4"].razon_social, sucursal.stock["4"], 15000,"oscuro")
vino= Producto(20225, "botella de vino 1.5L","licores", proveedores["5"].razon_social, sucursal.stock["5"], 20000, "tinto")
#Creación de un diccionario con los productos
productos= {"1":zapatillas, "2":jeans, "3":audifonos, "4":chocolates, "5":vino}

liliana= Cliente(1,"Liliana","Garmendia","liligc@gmail.com","10/02/2021", 80000)
clara=Cliente(2,"Clara", "Campos", "clara@gmail.com", "10/01/2019", 60000)
antonia=Cliente(3,"Antonia", "Garmendia", "anto@gmail.com", "10/01/2022", 100000)
valentina=Cliente(4,"Valentina", "Pasten", "vale@gmail.com", "20/01/2018", 50000)
constanza=Cliente(5,"Constanza", "Campos", "cony@gmail.com", "05/01/2020", 30000)
#Creación de un diccionario con los clientes
clientes={"1":liliana,"2":clara, "3":antonia, "4":valentina, "5":constanza}

