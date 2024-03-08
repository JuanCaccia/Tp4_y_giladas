import os
import io
import pickle
from registro import *


# Validadores y otros --------------------------------------------------------------------------------------------------


def menu():
    print("-" * 125)
    print("Bienvenido al menu de opciones:")
    print("Opción 1: Cargar los datos a un archivo binario o,si ya ha elegido esta opción"
          ",borrará el arreglo ya creado ")
    print("Opción 2: Cargar por teclado los datos de un ticket ")
    print("Opción 3: Mostrar todos los datos de todos los registros del archivo binario")
    print("Opción 4: Buscar todos los registros con patente 'p'(cargada por teclado)")
    print("Opción 5: Buscar registro por código de ticket (cargado por teclado)")
    print("Opción 6: Cantidad de vehículos de cada combinación posible entre tipo de vehículo  y país de cabina")
    print("Opción 7: Cantidad total de vehículos contados por cada tipo de vehículo posible y por cada país de cabina")
    print("Opción 8: Distancia promedio desde la última cabina recorrida entre todos los vehículos")
    print("Opción 0: Salir")
    print("-" * 125)

    return el_que_avisa_no_traiciona_rango(0, 8)


def el_que_avisa_no_traiciona_decision(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print("El archivo existente se borrará...")
        print("El que avisa no traiciona!!!")
        decision = input("Está seguro?\nIngrese 'SI' (escriba con mayúsculas, de lo contrario se tomará como un NO)")
        return decision
    else:
        return "SI"


def el_que_avisa_no_traiciona_rango(inf, sup):
    n = int(input(f"Ingrese un número entre {inf} y {sup}: "))

    while inf > n or sup < n:
        n = int(input(f"Ingrese un número entre '{inf}' y '{sup}', por favor: "))

    return n


def el_que_avisa_no_traiciona_positivo():
    num = int(input("Ingrese un número positivo: "))
    while num < 0:
        num = int(input("Ingrese un número positivo por favor: "))
    return num


def el_que_traiciona_no_avisa():
    num = int(input("Ingrese un número positivo: "))
    while num <= 0:
        num = int(input("Ingrese un número positivo por favor: "))
    return num


def el_que_traiciona_no_avisa_archivos(nombre_archivo):
    existe = False
    if os.path.exists(nombre_archivo):
        existe = True
    return existe


def mostrar_vector(vector):
    for i in vector:
        print(i)


def crear_registro(linea):
    if linea[-1] == "\n":
        linea = linea[:-1]
    caracteres = linea.split(",")
    codigo = caracteres[0]
    patente = caracteres[1]
    tipo_vehiculo = caracteres[2]
    forma_pago = caracteres[3]
    pais_cabina = caracteres[4]
    km_ult_cabina = caracteres[5]
    nacionalidad = identificar_pais(patente)
    ticket = Ticket(codigo, patente, nacionalidad, tipo_vehiculo, forma_pago, pais_cabina, km_ult_cabina)
    return ticket


# ----------------------------------------------------------------------------------------------------------------------

# Punto 1---------------------------------------------------------------------------------------------------------------


def carga_por_archivo(nombre_archivo):
    archivo_csv = open("peajes-tp4-corto.csv", "rt")
    archivo_bin = open(nombre_archivo, "wb")
    contador = 0
    for linea in archivo_csv:
        if contador > 1:
            ticket = crear_registro(linea)
            pickle.dump(ticket, archivo_bin)
        contador += 1
    archivo_csv.close()
    archivo_bin.flush()
    archivo_bin.close()
# ----------------------------------------------------------------------------------------------------------------------

# punto 2---------------------------------------------------------------------------------------------------------------


def patente_valida(patente):
    num = "1234567890"
    letra = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    patente_invalida = False
    for x in patente:
        if x not in num and x not in letra:
            patente_invalida = True

    return patente_invalida


def validador_patente():
    patente = input("Ingrese la patente solo con mayúsculas y números: ")
    patente_invalida = patente_valida(patente)
    while patente_invalida:
        patente = input("Ingrese la patente correctamente: ")
        patente_invalida = patente_valida(patente)

    return patente


def carga_por_teclado(nombre_archivo):
    archivo_csv = open("peajes-tp4-corto.csv", "rt")
    archivo_bin = open(nombre_archivo, "ab")
    print("Ingrese un número mayor a cero correspondiente al número de ticket...")
    codigo = el_que_traiciona_no_avisa()
    patente = validador_patente()
    print("A continuación para el tipo de vehículo ingrese un número entre 0 y 2...")
    tipo_vehiculo = el_que_avisa_no_traiciona_rango(0, 2,)
    print("A continuación para la forma de pago, ingrese in número entre 1 y 2...")
    forma_pago = el_que_avisa_no_traiciona_rango(1, 2)
    print("Ingrese un número entre 0 y 4 que indica el país donde"
          " está la cabina que hizo el cobro\n 0: Argentina \n 1: Bolivia \n 2: Brasil \n 3: Paraguay \n 4: Uruguay: ")
    pais_cabina = el_que_avisa_no_traiciona_rango(0, 4)
    print("A continuación para la distancia desde la última cabina ingrese un número positivo...")
    km_ult_cabina = el_que_avisa_no_traiciona_positivo()

    nacionalidad = identificar_pais(patente)

    ticket = Ticket(codigo, patente, nacionalidad, tipo_vehiculo, forma_pago, pais_cabina, km_ult_cabina)
    pickle.dump(ticket, archivo_bin)
    print(f"El ticket ha sido cargado a '{nombre_archivo}'...")
    archivo_csv.close()
    archivo_bin.flush()
    archivo_bin.close()


# ----------------------------------------------------------------------------------------------------------------------

# punto 3---------------------------------------------------------------------------------------------------------------


def identificar_pais(patente):
    num = "0123456789"
    letr = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    letra = 0
    for x in patente:
        if x in letr:
            letra += 1

    if letra == 4:
        if len(patente) == 6 and patente[4] in num and patente[5] in num:
            pais_auto = "Chile"
        elif patente[3] in num and patente[4] in letr:
            pais_auto = "Brasil"
        elif patente[2] in num and patente[3] in num and patente[4] in num:
            pais_auto = "Argentina"
        elif patente[4] in num and patente[5] in num and patente[6] in num:
            pais_auto = "Paraguay"
        else:
            pais_auto = "Otro"

    elif letra == 3:
        if patente[0] in letr and patente[1] in letr and patente[2] in letr:
            pais_auto = "Uruguay"
        else:
            pais_auto = "Otro"
    elif letra == 2:
        if patente[0] in letr and patente[1] in letr:
            pais_auto = "Bolivia"
        else:
            pais_auto = "Otro"
    else:
        pais_auto = "Otro"

    return pais_auto


def mostrar_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no extiste...")
        print()
        return
    tamanio = os.path.getsize(nombre_archivo)
    archivo = open(nombre_archivo, "rb")
    print(f"Mostrando el archivo '{nombre_archivo}'...")
    while archivo.tell() < tamanio:
        ticket = pickle.load(archivo)
        # print(ticket.argentino())
        print(ticket)
    archivo.close()
    print()
# ----------------------------------------------------------------------------------------------------------------------

# Punto 4---------------------------------------------------------------------------------------------------------------


def buscar_patente(nombre_archivo):
    patente = validador_patente()
    tamanio = os.path.getsize(nombre_archivo)
    archivo = open(nombre_archivo, "rb")
    fp_inicial = archivo.tell()
    archivo.seek(0, io.SEEK_SET)
    cantidad = 0
    while archivo.tell() < tamanio:
        ticket = pickle.load(archivo)
        if patente == ticket.patente:
            print(ticket)
            cantidad += 1
    if cantidad == 0:
        print("No se ha encontrado ningún registro con dicha patente...")
    archivo.seek(fp_inicial, io.SEEK_SET)
    archivo.close()


# ----------------------------------------------------------------------------------------------------------------------

# Punto 5---------------------------------------------------------------------------------------------------------------


def buscar_codigo(nombre_archivo):
    codigo = el_que_traiciona_no_avisa()
    tamanio = os.path.getsize(nombre_archivo)
    archivo = open(nombre_archivo, "rb")
    fp_inicial = archivo.tell()
    archivo.seek(0, io.SEEK_SET)
    se_encontro = None
    while archivo.tell() < tamanio:
        ticket = pickle.load(archivo)
        if str(codigo) == ticket.codigo:
            se_encontro = ticket
            break
    archivo.seek(fp_inicial, io.SEEK_SET)
    archivo.close()
    return se_encontro


# ----------------------------------------------------------------------------------------------------------------------

# Punto 6---------------------------------------------------------------------------------------------------------------


def matriz_trambolica(nombre_archivo):
    archivo = open(nombre_archivo, "rb")
    tamanio = os.path.getsize(nombre_archivo)
    matriz = []
    for i in range(3):
        matriz.append([0] * 5)
    while archivo.tell() < tamanio:
        ticket = pickle.load(archivo)
        for f in range(3):
            for c in range(5):
                if int(ticket.tipo_vehiculo) == f and int(ticket.pais_cabina) == c:
                    matriz[f][c] += 1
    return matriz


def mostrar_matriz(matriz):
    for f in range(3):
        for c in range(5):
            if matriz[f][c] != 0:
                print(f"Tipo de vehículo', '{f}' '\tForma', {c}, '\tCantidad:', {matriz[f][c]}")


# ----------------------------------------------------------------------------------------------------------------------

# Punto 7---------------------------------------------------------------------------------------------------------------


def totalizar_fila(matriz):
    for f in range(3):
        acum = 0
        for c in range(5):
            acum += matriz[f][c]
        print(f"El tipo de vehículo {f} registra {acum} vehículos")


def totalizar_columna(matriz):
    for c in range(5):
        acum = 0
        for f in range(3):
            acum += matriz[f][c]
        print(f"El país de cabina es {c} registra {acum} vehículos")
# ----------------------------------------------------------------------------------------------------------------------

# Punto 8---------------------------------------------------------------------------------------------------------------


def promedio(nombre_archivo):
    archivo = open(nombre_archivo, "rb")
    total = contador_tickets = 0
    tamanio = os.path.getsize(nombre_archivo)
    while archivo.tell() < tamanio:
        ticket = pickle.load(archivo)
        contador_tickets += 1
        total += int(ticket.km_ult_cabina)
    archivo.close()
    return round(total / contador_tickets, 2)


def crear_vector():
    archivo = open("peajes-tp4-corto.csv", "rt")
    contador = 0
    vector_tickets = []
    for linea in archivo:
        if contador > 1:
            ticket = crear_registro(linea)
            vector_tickets.append(ticket)
        contador += 1
    archivo.close()
    return vector_tickets


def shell_sort(vector):
    n = len(vector)
    h = 1
    while h <= n // 9:
        h = 3*h + 1
    while h > 0:
        for j in range(h, n):
            y = vector[j]
            k = j - h
            while k >= 0 and y.km_ult_cabina < vector[k].km_ult_cabina:
                vector[k + h] = vector[k]
                k -= h
            vector[k + h] = y
        h //= 3
    return vector


def shell_sort_vector(vector):
    n = len(vector)
    h = 1
    while h <= n // 9:
        h = 3*h + 1
    while h > 0:
        for j in range(h, n):
            y = vector[j]
            k = j - h
            while k >= 0 and y < vector[k]:
                vector[k + h] = vector[k]
                k -= h
            vector[k + h] = y
        h //= 3
    return vector


def mayor_al_promedio(prom, vector_ordenado):
    mayores_al_promedio = []
    for x in vector_ordenado:
        if int(x.km_ult_cabina) > prom:
            mayores_al_promedio.append(x)
    return mayores_al_promedio

# ----------------------------------------------------------------------------------------------------------------------


def main():
    op = None
    arch = "datos.dat"
    punto_6 = None
    while op != 0:
        op = menu()
        if op == 1:
            decision = el_que_avisa_no_traiciona_decision(arch)
            if decision == "SI":
                carga_por_archivo("datos.dat")
                print("Se ha creado el nuevo archivo con los datos...")

        elif op == 2:
            carga_por_teclado(arch)

        existe = el_que_traiciona_no_avisa_archivos(arch)

        if existe:
            if op == 3:
                mostrar_archivo(arch)

            elif op == 4:
                buscar_patente(arch)

            elif op == 5:
                punto_5 = buscar_codigo(arch)
                if punto_5 is None:
                    print("No se ha encontrado dicho registro...")
                else:
                    print("El registro encontrado es...")
                    print(punto_5)

            elif op == 6:
                matriz = matriz_trambolica(arch)
                mostrar_matriz(matriz)
                punto_6 = True

            elif op == 7:
                if punto_6:
                    matriz = matriz_trambolica(arch)
                    print("Por tipo de vehículos:")
                    totalizar_fila(matriz)
                    print("Por país de cabina:")
                    totalizar_columna(matriz)
                else:
                    print("Primero debe cargar la matriz mediante la opción 6...")
            elif op == 8:
                prom = promedio(arch)
                print(f"El promedio de kilometros recorridos desde la última cabina es {prom}")
                vector = crear_vector()
                vector_ordenado = shell_sort(vector)
                mayores = mayor_al_promedio(prom, vector_ordenado)
                print(f"Y los que tienen mas kilometros recorridos a '{prom}' es...")
                mostrar_vector(mayores)

            elif op == 0:
                print("Salió del programa")
        else:
            print("No se han cargado datos de algún archivo o manualmente...\n"
                  "Ejecute la opción 1 o 2 del programa...")


if __name__ == '__main__':
    main()
