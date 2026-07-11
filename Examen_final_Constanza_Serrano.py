# ---------- DICCIONARIOS ----------

productos = {
    "M001": ["Alimento Premium", "comida", "DogPlus", 10, True, False],
    "M002": ["Arena Aglomerante", "higiene", "CatClean", 8, False, False],
    "M003": ["Snack Dental", "snack", "BiteJoy", 1, True, True],
    "M004": ["Shampoo Suave", "higiene", "PetCare", 0.5, False, True],
    "M005": ["Correa Nylon", "accesorio", "WalkPro", 0.3, True, False],
    "M006": ["Cama Mediana", "accesorio", "CozyPet", 2, False, False]
}

stock = {
    "M001": [32990, 12],
    "M002": [9990, 0],
    "M003": [5490, 25],
    "M004": [7990, 5],
    "M005": [11990, 7],
    "M006": [24990, 3]
}


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))

            if 1 <= opcion <= 6:
                return opcion

            print("Debe seleccionar una opción válida")

        except ValueError:
            print("Debe seleccionar una opción válida")


def buscar_codigo(codigo, stock):
    codigo = codigo.upper()
    for c in stock:
        if c.upper() == codigo:
            return True
    return False


def unidades_categoria(categoria, productos, stock):

    total = 0
    categoria = categoria.lower()

    for codigo in productos:
        if productos[codigo][1].lower() == categoria:
            total += stock[codigo][1]

    print("El total de unidades disponibles es:", total)


def busqueda_precio(p_min, p_max, productos, stock):
    lista = []

    for codigo in stock:
        precio = stock[codigo][0]
        unidades = stock[codigo][1]

        if precio >= p_min and precio <= p_max and unidades > 0:
            nombre = productos[codigo][0]
            lista.append(nombre + "--" + codigo)

    lista.sort()

    if len(lista) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        print("Los productos encontrados son:", lista)


def actualizar_precio(codigo, nuevo_precio, stock):
    codigo = codigo.upper()

    if buscar_codigo(codigo, stock):
        stock[codigo][0] = nuevo_precio
        return True

    return False


## ------- FUNCIONES DE VALIDACIÓN --------##

def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True


def validar_peso(peso_texto):
    try:
        peso = float(peso_texto)
    except ValueError:
        return False
    return peso > 0


def validar_si_no(valor):
    valor = valor.strip().lower()
    return valor == "s" or valor == "n"


def validar_precio(precio_texto):
    try:
        precio = int(precio_texto)
    except ValueError:
        return False
    return precio > 0


def validar_unidades(unidades_texto):
    try:
        unidades = int(unidades_texto)
    except ValueError:
        return False
    return unidades >= 0


## ------- AGREGAR PRODUCTO --------##

def agregar_producto(codigo, nombre, categoria, marca, peso, importado,
                      cachorro, precio, unidades, productos, stock):

    codigo = codigo.upper()

    if buscar_codigo(codigo, stock):
        return False

    productos[codigo] = [
        nombre,
        categoria,
        marca,
        peso,
        importado,
        cachorro
    ]

    stock[codigo] = [
        precio,
        unidades
    ]

    return True


## ----- ELIMINAR PRODUCTO -----##

def eliminar_producto(codigo, productos, stock):
    codigo = codigo.upper()

    if buscar_codigo(codigo, stock):
        del productos[codigo]
        del stock[codigo]
        return True

    return False


# -------------- PROGRAMA PRINCIPAL --------------- #

while True:

    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese categoría: ")
        unidades_categoria(categoria, productos, stock)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min < 0 or p_max < 0:
                    print("Los precios deben ser mayores o iguales a cero")
                    continue
                if p_min > p_max:
                    print("El precio mínimo debe ser menor o igual al máximo")
                    continue
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(p_min, p_max, productos, stock)

    elif opcion == 3:
        while True:
            codigo = input("Ingrese código del producto: ")
            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                    else:
                        print("El precio debe ser un entero positivo")
                except ValueError:
                    print("Debe ingresar un valor entero")
            resultado = actualizar_precio(codigo, nuevo_precio, stock)
            if resultado:
                print("Precio actualizado")
            else:
                print("El código no existe")
            respuesta = input("¿Desea actualizar otro precio (s/n)?: ")
            if respuesta.lower() == "n":
                break

    elif opcion == 4:
        datos_validos = True

        codigo = input("Ingrese código del producto: ")
        if not validar_texto(codigo):
            print("El código no puede estar vacío")
            datos_validos = False

        if datos_validos:
            nombre = input("Ingrese nombre: ")
            if not validar_texto(nombre):
                print("El nombre no puede estar vacío")
                datos_validos = False

        if datos_validos:
            categoria = input("Ingrese categoría: ")
            if not validar_texto(categoria):
                print("La categoría no puede estar vacía")
                datos_validos = False

        if datos_validos:
            marca = input("Ingrese marca: ")
            if not validar_texto(marca):
                print("La marca no puede estar vacía")
                datos_validos = False

        if datos_validos:
            peso_input = input("Ingrese peso (kg): ")
            if not validar_peso(peso_input):
                print("El peso debe ser un número mayor que cero")
                datos_validos = False
            else:
                peso_kg = float(peso_input)

        if datos_validos:
            importado_input = input("¿Es importado? (s/n): ")
            if not validar_si_no(importado_input):
                print("Debe ingresar 's' o 'n'")
                datos_validos = False
            else:
                es_importado = importado_input.lower() == "s"

        if datos_validos:
            cachorro_input = input("¿Es para cachorro? (s/n): ")
            if not validar_si_no(cachorro_input):
                print("Debe ingresar 's' o 'n'")
                datos_validos = False
            else:
                es_para_cachorro = cachorro_input.lower() == "s"

        if datos_validos:
            precio_input = input("Ingrese precio: ")
            if not validar_precio(precio_input):
                print("El precio debe ser un entero mayor que cero")
                datos_validos = False
            else:
                precio = int(precio_input)

        if datos_validos:
            unidades_input = input("Ingrese unidades: ")
            if not validar_unidades(unidades_input):
                print("Las unidades deben ser un entero mayor o igual a cero")
                datos_validos = False
            else:
                unidades = int(unidades_input)

        if datos_validos:
            resultado = agregar_producto(codigo, nombre, categoria, marca,
                                          peso_kg, es_importado, es_para_cachorro,
                                          precio, unidades, productos, stock)
            if resultado:
                print("Producto agregado")
            else:
                print("El código ya existe")

    elif opcion == 5:
        codigo = input("Ingrese código del producto: ")
        resultado = eliminar_producto(codigo, productos, stock)
        if resultado:
            print("Producto eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break
