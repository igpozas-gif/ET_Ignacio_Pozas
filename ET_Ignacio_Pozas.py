
prendas = {
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
}

bodega = {
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2],
}

def leer_opcion():
    print ("========== MENÚ PRINCIPAL ========== \n1. Unidades por categoría\n2. Búsqueda de prendas por rango de precio\n3. Actualizar precio de prenda\n4. Agregar prenda\n5. Eliminar prenda\n6. Salir\n=====================================")
    try:
        opcion = int(input("Ingrese una opción del menú"))
        if 0 < opcion < 7:
            return opcion
        else:
            print ("Debe seleccionar una opción válida")
    except ValueError:
        print ("Debe seleccionar una opción válida")

def unidades_categoria(categoria_buscar, prendas, bodega):
    prenda_por_categoria = 0
    for codigo in prendas:
        if prendas[codigo][1].lower() == categoria_buscar.lower():
            prenda_por_categoria += bodega[codigo][1]
    print (f"Prendas en bodega para la categoría{categoria_buscar}:{prenda_por_categoria}")

def busqueda_precio(precio_min, precio_max, prendas, bodega):
    productos_en_rango = []
    for codigo,datos in prendas.items():
        if bodega [codigo][0] > precio_min and bodega[codigo][0] < precio_max and bodega[codigo][1] > 0:
            productos_en_rango.append(([prendas[codigo][1], codigo]))
    for productos in productos_en_rango:
        print (f"{productos[0]} -- {productos[1]}")

while True:
    opcion = leer_opcion()   
    if opcion == 1:
        categoria_buscar = input ("Ingrese una categoría de prenda para buscar")
        unidades_categoria (categoria_buscar, prendas, bodega)
    elif opcion == 2:
        try:
            precio_min = int(input("Ingrese el precio mínimo para buscar"))
            precio_max =int(input("Ingrese el precio máximo para buscar"))
            if precio_min >= 0 and precio_max >= 0 and precio_min < precio_max:
                busqueda_precio(precio_min, precio_max, prendas, bodega)
        except ValueError:
            print ("Debe ingresar valores enteros")