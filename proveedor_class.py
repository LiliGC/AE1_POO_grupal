class Proveedor:

    def __init__(self, rut, nombre_legal, razon_social, pais, juridica):
        self.rut=rut
        self.nombre_legal= nombre_legal
        self.razon_social= razon_social
        self.pais= pais
        self.juridica=juridica
    
    def __str__(self):
        return f"Datos proveedor:\n {self.razon_social}\t{self.rut}\t{self.juridica}\t"


prov1= Proveedor("72635988-7", "Danilo Mardones", "Adidas_SA", "Chile", "juridica")


print(prov1)