from main import menu as god_menu, shell_sort_vector as shell
from datetime import datetime, timedelta
import random, json, csv, re
import numpy as np
n_1 = 5
n_2 = 1
# n_2 = "1"

numeros = [49, 73, 11, 30, 82, 67, 5, 91, 62, 14, 20, 33, 55, 88, 42, 97, 2, 78, 60, 25, 44]

try:
    print(f"las suma es: {n_1 + n_2}")
    print("pindongan´t")

except TypeError as error:
    print(error)
    print("pindonga")

'''
except Exception as error:
    print(error) 
'''
# god_menu()
print(shell(numeros))

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


print(sum_10(40)(20))  # otra forma de llamar teniendo un closure


'''
def sum_10():  # Una funcion
    def sumar(num):  # que define otra funcion
        return num + 10
    return sumar  # Y la retorna


suma_closures = sum_10()  # en esta variable se guarda funcion que retorna sum_10
print(suma_closures(30))  # por eso se le tiene que pasar un parametro
'''


# Map: necesita simpre un conjuto iterable para recorrerlo y modificarlo segun la funcion que le pasamos
def triplicar(numero):
    return numero * 3


print(list(map(triplicar, numeros)))

# Filter: Necesita un conjunto iterable para recorrerlo y seleccionar un elelmneto
# segun obtenga un true o false de la funcion que le pasamos


def menor_50(numero):
    if numero < 50:
        return True
    return False


print(list(filter(menor_50, numeros)))
print(list(filter(lambda num: num < 50, numeros)))  # con lambdas

# sets

sets = {2, 4, 9, 0, 12}

sets.add(2)
sets.add(5)
sets.add(17)
sets.add(4)

'''
Ordenación y Duplicados:

Listas: Mantienen el orden de los elementos y permiten duplicados. Puedes acceder a los elementos de una lista 
utilizando índices.
Sets: No mantienen ningún orden específico y no permiten duplicados. Los elementos en un conjunto están únicos.

Sintaxis:

Listas: Se definen utilizando corchetes [] y los elementos se separan por comas.
Sets: Se definen utilizando llaves {} o la función set() y los elementos se separan por comas.

Mutabilidad:

Listas: Son mutables, lo que significa que puedes cambiar, agregar o eliminar elementos después de crear la lista.
Sets: Son mutables, pero los elementos individuales no son mutables. No puedes cambiar un elemento específico en un 
conjunto, pero puedes agregar o eliminar elementos.
Operaciones:

Listas: Ofrecen una variedad de operaciones como indexación, rebanado, concatenación y métodos específicos como append()
, extend(), insert(), remove(), pop(), entre otros.
Sets: Son útiles para realizar operaciones de conjuntos como unión, intersección, diferencia, etc. Los sets también
tienen métodos para agregar elementos (add()), eliminar elementos (remove(), discard()), comprobar la membresía (in),etc

Rendimiento:

Listas: Las listas tienen un rendimiento eficiente para la indexación y el acceso a elementos por posición, pero pueden 
ser menos eficientes para comprobar la existencia de un elemento debido a que se recorre secuencialmente.
Sets: Los sets tienen un rendimiento muy eficiente para comprobar si un elemento está presente, ya que utilizan una
estructura de datos hash subyacente para el almacenamiento.

En resumen, las listas son una buena opción cuando necesitas una colección ordenada y con elementos duplicados, mientras
que los sets son útiles cuando necesitas garantizar la unicidad de elementos y/o realizar operaciones de conjuntos 
eficientes.
'''

if 2 in sets:
    print("si esta wachin")

print(sets)


# manejo de ficheros

texto = open("texto.txt", "r+")  # El 'r+' no sobreescribe un nuevo archivo, en cambio el 'w+' si lo hace

# texto.writelines("\npinga pinga pinga pinga pinga")  # cadda vez que se ejecuta el programa agrega una linea xd
# texto.write("\notra linea")

texto.close()
with open("texto.txt", "r+") as leer_texto:
    for x in leer_texto:
        print(x[:-1])

# json


json_texto = open("texto.json", "r+")

json_test = {
    "Nombre": "Juan",
    "Apellido": "Caccia",
    "Edad": 19,
    "Apodo": "GODinez",
    "Hobies": ["Leer", "Ir al gym", "Rodar la caprichosa"]
}

json.dump(json_test, json_texto, indent=4)

json_texto.close()

with open("texto.json", "r+") as lectura_json:
    for line in lectura_json:
        print(line[:-1])

json_dict = json.load(open("texto.json", "r+"))
print(json_dict)

print(json_dict["Nombre"])


# csv ,se importa csv

arch_csv = open("texto.csv", "r+")

writer = csv.writer(arch_csv)

writer.writerow(["juan", "Caccia", 19, "ING"])
writer.writerow(["pedro", "pedroide", 19.3, "ING"])
writer.writerow(["pepinho", "", "", "soccer player"])

arch_csv.close()

with open("texto.csv", "r+") as lectura_csv:
    for line in lectura_csv:
        print(line[:-1])


# Expresiones regulares (Se importa "re")

un_string = "este es un string String, xd XD"
otro_string = "este no es un string, xdn't xdn't, es el 5to string"


print(re.match("este es", un_string))  # empieza a mirar desde el comienzo del string
print(re.match("xd", un_string, re.I))

'''
re.A (ASCII-only matching)
re.I (ignore case)
re.L (locale dependent)
re.M (multi-line)
re.S (dot matches all)
re.U (Unicode matching)
re.X (verbose)
'''

matcheao = re.match("Este NO", otro_string, re.I)

print(matcheao.span())  # Con el .span() tenemos el rango en el que se encuentra dicha cadena de texto
print(otro_string[0:7])

'''
start, end = matcheao.span()
print(otro_string[start:end])
'''

print(re.search("xd", un_string, re.I))  # Este busca en cualquier parte del texto
print((re.search("xd", un_string, re.I)).span())

print(re.findall("xd", un_string, re.I))  # Este cuenta la cantidad de veces que se encontro y los mete en una lista
print(len(re.findall("xd", un_string, re.I)))

print(re.split(",", un_string))  # Separa ,segun el simbolo que se le indique, dentro de una lista

print(re.sub("este no", "este si que no",  otro_string))
print(re.sub("xd|XD", "xdn't",  un_string))
print(re.sub("[s|S]tring", "string",  un_string))


pattern = r"[s|S]tring|xd"

print(re.findall(pattern, un_string))  # Le estamos pasando los patrones que queremos buscar

print(re.findall("[0-9]", otro_string))
# pattern = r"[0-9]"
# print(re.findall(pattern, otro_string))


pattern = r"\d"  # Busca todos los numeros
print(re.findall(pattern, otro_string))

pattern = r"\D"  # Busca todos los caracteres
print(re.findall(pattern, otro_string))

# Validacion de email

email = "juanmacaccia@gmail.com"
# email = "juanmacaccia@gmail"  # en este caso como falta la continuacion despues de un '.' no lo toam como un email
# email = "juanmacaccia@gmail."  #lo mismo pero ddeberia haber algo despues del '.'
# pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"  # con el '^' indica que comienza con eso, con el '+@' indica que despues sigue un '@' y los caracteres que se le indica, coon el '\.' indica que escapa a todos los caracteres excepto los que se les indica, en '$' tiene en cuenta todo lo que esta despues del '.'
pattern = r"^([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(?:com|com.ar))"

"""
MEjor pagina para expresiones regulares:
https://regex101.com
NO hay que pasarle la 'r' ni las comillas
"""
print(re.findall(pattern, email))
print(re.match(pattern, email))
print(re.search(pattern, email))


'''
    []: A set of characters
    
    [a-c] means, a or b or c
    
    [a-z] means, any letter from a to z
    
    [A-Z] means, any character from A to Z
    
    [0-3] means, 0 or 1 or 2 or 3
    
    [0-9] means any number from 0 to 9
    
    [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
    
    \: uses to escape special characters
    
    \d means: match where the string contains digits (numbers from 0-9)
    
    \D means: match where the string does not contain digits
    
    . : any character except new line character(\n)
    
    ^: starts with
    
    r'^substring' eg r'^love', a sentence that starts with a word love
    
    r'[^abc] means not a, not b, not c.
    
    $: ends with
    
    r'substring$' eg r'love$', sentence that ends with a word love
    
    *: zero or more times
    
    r'[a]*' means a optional or it can occur many times.
    
    +: one or more times
    
    r'[a]+' means at least once (or more)
    
    ?: zero or one time
    
    r'[a]?' means zero times or once
    
    {3}: Exactly 3 characters
    
    {3,}: At least 3 characters
    
    {3,8}: 3 to 8 characters
    
    |: Either or
    
    r'apple|banana' means either apple or a banana
    
    (): Capture and group
'''


# Manejo de arhivos y paquetes (corte tu vieja)
# con https://pypi.org

numpy = np.version.version

numpy_arrays = np.array(numeros)

print(numeros * 2)
print(numpy_arrays * 2)  # Trabaja con toda la lista sin tener que iterarla anacheiiiiiii
print(np.split(numpy_arrays, 3))  # divide en partes iguales solo si es posible
