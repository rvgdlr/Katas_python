 # 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def cadena_frecuencias(texto):
    frecuencias = {} 
    for letra in texto:
        if letra !="": # Para no considerar espacios
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doble_lista(numeros):
    return list(map(lambda x: x*2, numeros))


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def lista_palabra_objetivo(lista_palabras, objetivo):
    return[palabra for palabra in lista_palabras if objetivo in palabra]

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista_1,lista_2):
    return list(map(lambda x,y:x-y, lista_1,lista_2))

# 5. Función que tome una lista de números como parámetro y un valor opcional nota_aprobado que por defecto es 5.

def calificar_notas(calificacion, nota_aprobado=5):
    if calificacion:
        media = sum(calificacion)/len(calificacion) #Calculo de la media 
        estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return(media, estado)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva

def factorial(n):
    if n<0:
        return("Error el factorial no está definido para números negativos")
    if n==0 or n==1:
        return 1
    return (n*factorial(n-1))

# 7. Genera una función que convierta una lista de tuplas en una lista de strings.Usar la función map()

def tuplas_a_strings(tuplas):
    return list(map(lambda x:''.join(map(str,x)),tuplas))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Aségurate de mostrar un mensaje indicando si la división fue exitosa o no.

def programa_division():
    try:
        a = float(input("Introduce el primer número:"))
        b = float(input("Introduce el segundo número:"))
    
        division = a/b
    except ValueError:
        print("Error:ingresar solo valores númericos")
    except ZeroDivisionError:
        print("Error:No se puede dividir entre cero")
    else:
        print(f"División exitosa:el resultado es:{division}")


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache","Tibbre","Serpiente Pitón","Cocodrilo","Oso"]. Usa la función filter()

def mascotas_permitidas(lista_mascotas):
    prohibidas = ["Mapache","Tigre","Serpiente Pitón","Cocodrilo","Oso"] 
    return list(filter(lambda mascota: mascota not in prohibidas,lista_mascotas))

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el erro adecuadamente

def promedio_lista(números):
    if len(números) ==0:
        raise Exception("La lista está vacía.")
    return sum(números)/len(números)

# 11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no númerico o un valor fuera de rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente

def programa_edad():
    try:
        edad = input("Por favor, introducir edad:")
        edad= int(edad)
        if edad<0 or edad > 120:
            raise ValueError ("La edad debe de estar entre 0 y 120")
        print(f"Tue edad es: {edad} años")
    except ValueError as e:
        print(f"Error: {e}")

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabra(frase):
    palabras = frase.split() # Para dividir la frase en una lista de palabras
    longitud = list(map(len, palabras))
    return longitud

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usar la funció map()

def tupla_minus_mayus(conjunto):
    letras_unicas = set(conjunto) #para eliminar letras repetidas
    return list(map(lambda letra:(letra.upper(), letra.lower()),letras_unicas))

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_especificas(lista_palabras,letra_especifica):
    return list(filter(lambda palabra:palabra.lower().startswith(letra_especifica.lower()),lista_palabras))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada

def suma_tres(lista_numeros):
    return list(map(lambda x:x+3, lista_numeros))

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas(texto, n):
    palabras =  texto.split() #Dividir el texto en palabras
    return list(filter(lambda palabra:len(palabra) > n, palabras))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos(572). Usa la función reduce()

from functools import reduce
def cambio_lista_numeros(dígitos):
    return reduce(lambda x, y: x*10 +y, dígitos)

# 18. Escribe un programa en Python que cree un alista de diccionarios que contega información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def estudiantes_mejor_calificacion (diccionario):
    return list(filter(lambda e: e["calificacion"] >= 90, diccionario))


# 19. Crea una función lambda que filtre los números impares de una lista dada

def impares(lista_números):
    return list(filter(lambda x:x%2 !=0, lista_números))

# 20. PAra una lista con elementos tipo integer y string obtén una nueva lista sólo cono los valores int. Usa la función filter()

def lista_int(elementos):
    return list(filter(lambda x: isinstance(x, int), elementos)) # La función isinstance devuelve True si el valor es del tipo indicado, en este caso int

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def cubo_numero(numero):
    cubo = lambda n: n**3
    return cubo(n)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce()

from functools import reduce
def producto_total(lista_numerica):
    return reduce(lambda x,y: x*y, lista_numerica)

# 23. Concatena una lista de palabras. Usa la función reduce()

from functools import reduce
def concatenar(lista_palabras):
    return reduce(lambda x, y: x + " " + y, lista_palabras)

# 24. Calcular la diferencia total en los valores de una lista. Usa la función reduce()

from functools import reduce
def diferencia_total(lista_valores):
    return reduce(lambda x, y: x-y, lista_valores)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada

def contar_caracteres(texto):
    return len(texto)

# 26. Crea una función lambda que calcule el resto de  la división entre dos números dados

def resto_division(n_1,n_2):
    resto = lambda x, y: x/y
    return resto(a, b)

# 27 Crea una función que calcule el promedio de una lista de números

def calculo_promedio(numeros):
    if len(numeros)==0:
        return ("El valor no se puede calcular") # verifica que la lista no esta vacía y de error por división 0
    suma = sum(numeros)
    promedio = suma/len(numeros)
    return promedio

# 28. Crea una función que busque y devuelva el primer elemento duplicado de una lista dada

def elementos_duplicados(lista_elementos):
    vistos = set() #Creamos para guardar los elementos ya vistos y compararlos 
    for elemento in lista_elementos:
        if elemento in vistos:
            return elemento
        else:
            vistos.add(elemento)
    return None

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare rodos los caracteres con el carácter #, excepto los últimos cuatro

def variable_cadena(variable):
    texto = str(variable)  #Para convertir cualquier número en texto
    if len(texto)<= 4:
        return texto
    cantidad_ocultar = len(texto)-4
    oculto= '#'*cantidad_ocultar + texto[-4:]
    return oculto


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden

def anagramas(palabra_1,palabra_2):
    palabra_1 = palabra_1.lower()
    palabra_2 = palabra_2.lower()
    if len(palabra_1) != len(palabra_2):
        return "No son anagramas"
    ordenada_1 = sorted(palabra_1) #ordenar las letras alfabéticamente
    ordenada_2 = sorted(palabra_2)
    return ordenada_1 == ordenada_2























    
















                



