productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
while True:
 print("*** MENU PRINCIPAL ***")
 print("1. Stock marca.")
 print("2. Búsqueda por precio.")
 print("3. Eliminar producto.")
 print("4. Salir.")

 opcion = int(input("ingrese una opcion: "))
 if opcion == 1:
    print("ingrese una marca: ")
    def stock_marca(marca):
        total=0
        for modelo, datos in stock.items():
            if marca.lower() == datos[0].lower():
               total+=stock[modelo][1]
            print(f"hay {total} en stock")

 elif opcion == 2:
    def búsqueda_precio(p_min, p_max):

 elif opcion == 3:
    def eliminar_producto(producto)
       if productos=True:
        print("se ha eliminado el producto con exito!")
        if not eliminar_producto:
           print("no se ha podido eliminar el producto.")
 elif opcion == 4:
    print("gracias por elegirnos. Hasta luego!")

 elif opcion <4:
    ValueError("porfavor ingrese una opcion del 1-4")