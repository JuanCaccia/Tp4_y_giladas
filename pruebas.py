from main import menu as god_menu, shell_sort_vector as shell
from datetime import datetime, timedelta
import random
n_1 = 5
n_2 = 1
# n_2 = "1"

vector = [49, 73, 11, 30, 82, 67, 5, 91, 62, 14, 20, 33, 55, 88, 42, 97, 2, 78, 60, 25]

try:
    print("pindongan´t")
    print(f"las suma es: {n_1 + n_2}")

except TypeError as error:
    print("pindonga")
    print(error)

'''
except Exception as error:
    print(error) 
'''
# god_menu()
print(shell(vector))

now = datetime.now()


def print_dia(fecha):
    print(f"El Timestamp: {fecha.timestamp()} Corresponde a:")  # Forma unica de representar el tiempo
    print(f"Año: {fecha.year}")
    print(f"Mes: {fecha.month}")
    print(f"Dia: {fecha.day}")
    print(f"Hora: {fecha.hour}")
    print(f"Minuto: {fecha.minute}")
    print(f"Segundo: {fecha.second}")


print_dia(now)

mi_cumple = datetime(2024, 3, 31)

print_dia(mi_cumple)


diff = mi_cumple - now  # Haciendo esto se podria saber el restante de dias hasta una fecha concreta
print(diff)

# el timedelta se utiliza mas que naada para estableces franjas de tiempo no tanto fechas
inicio = timedelta(200, 100, 333, weeks=12)
final = timedelta(440, 111, 333, weeks=15)
print(final - inicio)
print(final + inicio)


def generar_randon():
    i = random.randint(0, 100)
    return i


lista = [generar_randon() for i in range(10)]
'''
lista = [generar_randon() for i in range(generar_randon())]  # genera una lista de largo random con elementos random 
'''
print(lista)


# saber los numeros primos en un rango determinadoh
def primo():
    for i in range(1, 101):
        divisible = False

        for x in range(2, i):
            if i % x == 0:
                divisible = True

        if not divisible:
            print(i)


primo()
