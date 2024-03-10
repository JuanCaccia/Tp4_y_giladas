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

        if i >= 2:
            for x in range(2, i):
                if i % x == 0:
                    divisible = True

            if not divisible:
                print(i)


primo()


# volteatestos
def voltear_texto(texto):

    volteao = ""
    for x in range(0, len(texto)):
        volteao += texto[len(texto) - x - 1]

    return volteao


print(voltear_texto("Pinga de mono"))


# closures

def sum_10(otro_num):  # Una funcion
    def sumar(num):  # que define otra funcion
        return num + 10 + otro_num
    return sumar  # Y la retorna


suma_closures = sum_10(20)  # en esta variable se guarda funcion que retorna sum_10
print(suma_closures(30))  # por eso se le tiene que pasar un parametro


'''
def sum_10():  # Una funcion
    def sumar(num):  # que define otra funcion
        return num + 10
    return sumar  # Y la retorna


suma_closures = sum_10()  # en esta variable se guarda funcion que retorna sum_10
print(suma_closures(30))  # por eso se le tiene que pasar un parametro
'''