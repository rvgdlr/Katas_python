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

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en la lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, d elo contrario, se lanza una excepción

def buscar_nombre():
    try:
        lista_nombres = input("Escriba una lista de nombres: ")
        nombre_a_buscar = input("Nombre que quiere buscar: ")
        if nombre_a_buscar in lista_nombres:
            print(f"El nombre {nombre_a_buscar} fue encontrado en la lista")
        else:
            raise ValueError (f"El nombre {nombre_a_buscar} no se encuentra en la lista")
    except ValueError as error:
        print (error)

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def nombre_puesto(nombre, lista_empleados):
    for empleado in lista_empleados:
        if empleado ["nombre"].lower() == nombre.lower():
            return f"{empleado["nombre"]} trabaja como {empleado["puesto"]}"


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas

def suma_listas(lista_1, lista_2):
    return list(map(lambda x, y: x + y, lista_1, lista_2))

# 34. Crea la clase arbol, define un árbol genérico con un tronco y ramas atributos. Los métdos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implantar estos métodos para manipular la estrucutra del arbol

class Arbol:
    def __init__(self):
        #1 . Iniciar tronoco desde 1 y lista vacía pra las ramas
        self.tronco = 1   
        self.ramas = [] 

    def crecer_tronco(self):
        self.tronco +=1 # 2. Aumenta la longitud del tronco en una unidad
        print ("El tronco ha crecido. Longitud actual:", self.tronco)
    
    def nueva_rama(self):
        self.ramas.append(1) # 3. Agrega una nueva rama de longitud
        print("Nueva rama añadida. Total de ramas:", len(self.ramas))
    
    def crecer_ramas(self):
        # 4. Aumenta la longitud de todas las ramas en una unidad
        if not self.ramas:
            print("No hay ramas que hacer crecer")
            return
        self.ramas = [rama + 1 for rama in self.ramas]
        print("Todas las ramas han crecido una unidad")
    
    def quitar_rama(self, posicion):
        # 5. Elimina una rama en una posición específica, comenzando desde 1
        if 1 <= posicion <= len(self.ramas):
            rama_eliminada = self.ramas.pop(posicion - 1)
            print(f"Se ha eliminado la rama número {posicion} longitud: {rama_eliminada}")
        else:
            print("Posición no válida. No se ha eliminado ningua rama")

    def info_arbol(self):
        # 6. Muestra información completa del árbol"
        print("\n Información del arbol:")
        print(f" - Longitud del tronco: {self.tronco}")
        print(f" - Número de ramas; {len(self.ramas)}")
        print(f" - Longitudes de las ramas: {self.ramas if self.ramas else 'sin ramas todavía'}")

# CASOS DE USO
## 1. Crear un árbol
mi_arbol = Arbol()
print("Se ha plantado un árbol nuevo")

## 2. Hacer crecer el tronco del arbol una unidad
mi_arbol.crecer_tronco()

## 3. Añadir una nueva rama al árbol
mi_arbol.nueva_rama()

## 4. Hacer crecer todas las ramas del árbol una unidad
mi_arbol.crecer_ramas()

## 5. Añadir dos nuevas ramas al árbol
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

## 6. Retirar la rama situada en la posición 2
mi_arbol.quitar_rama(2)

## Obtener información sobre el árbol
mi_arbol.info_arbol()


# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero dede otro usuario y agregar dinero al saldo

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # 1. Inicializar un usuario con su nombre, slado y si tien o no cuenta corriente mediante true y false
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        # 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse
        if not self.cuenta_corriente:
            raise Exception(f"{self.nombre} no tiene cuenta corrriente. No puede retirar dienero")
        if cantidad > self.saldo:
            raise Exception(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo restante {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        # 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poderse hacer.
        if not otro_usuario.cuenta_corriente:
            raise Exception(f"{otro_usuario.nombre} no teine cuenta corriente. No puede transferir dinero.")
        if cantidad > otro_usuario.saldo:
            raise Exception(f"{otro_usuario.nombre} no tienen suficiente saldo para transferir {cantidad}")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print (f"{otro_usuario.nombre} ha transferido {cantidad} a {self.nombre}")
        print (f"Nuevo saldo de {self.nombre}: {self.saldo}")
        print (f"Nuevo saldo de {otro_usuario.nombre}: {otro_usuario.saldo}")

    def agregar_dinero(self, cantidad):
        # 4. Implimentar el métdo agregar_dinero para agregar dinero al saldo del usuario
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Nuevo saldo:{self.saldo}")

# CASOS DE USO
## 1 Crear dos usuarios
alicia = UsuarioBanco("alicia", 100, True)
bob = UsuarioBanco("bob", 50, True)

## 2. Agregar 20 unidades de saldo a bob
bob.agregar_dinero(20)

## 3. Hacer una tranferencia de 80 unidades desde bob a alicia
alicia.transferir_dinero(bob, 80)

## 4. Retirar 50 unidades de saldo a alicia
alicia.retirar_dinero(50)

# 37. Crea una función llamdad procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabras. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto

## 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario

def contar_palabras(texto):
    palabras = texto.lower().split() #Texto en minúsculas y separamos por espacios
    conteo = {} # Creo un diccionario vacío
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

## 2. Crear una función reemplazar_palabras para reempalzr una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplaxo de palabras

def reemplazar_palabras (texto, palabra_original, palabra_nueva):
    nuevo_texto = texto.replace(palabra_original, palabra_nueva)
    return nuevo_texto

## 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada

def eliminar_palabra(texto, palabra_eliminar):
    palabras = texto.split()
    palabras_filtradas =[p for p in palabras if p != palabra_eliminar]
    nuevo_texto = " ".join(palabras_filtradas)
    return nuevo_texto

## 4. Crear una función procesar_texto que tome un texto, una opción ente "contar", "reemplazar", "eliminar" y un número de argumentos variables según la opción indicada

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Debes indicar palabra_original y palabra_nueva para reemplazar")

        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Debes de indicar la palabra a elimianar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa: 'contar', 'reemplazar' o'eliminar'")
    
# CASO DE USO. Comprueba el funcionamiento completo de la función procesar_texto
## 1. Contar palabras
print("Conteo de palabras:")
print(procesar_texto(texto_original, "contar"))

## 2. Reemplazr palabras
print("\n reemplazo de palabra:")
print(procesar_texto(texto_original, "reemplazar", "Python","Programa"))

## 3. Eliminar palabra
print("\n Eliminación de palabra:")
print(procesar_texto(texto_original, "eliminar", "fácil"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario

hora = input("Introduce la hora en formato 0 a 23 horas: ")
if hora.isdigit():
    hora = int(hora)
    if 0 <= hora <= 23:
        if 6 <= hora <= 12:
            print("Es de día")
        elif 13 <= hora <= 19:
            print("Es de tarde")
        else:
            print("Es de noche")
    else:
        print("La hora debe de estar entre 0 y 23")
else:
    print ("Por favor, indroduzca un número válido")

# 39. Escribe un programa que determine que califiación en texto tiene un alumno en base a su calificación numérica. Las reglas de califiación son: 0-69 insuficiente, 70 a 79 bien, 80 a 89 muy bien, 90 a 100 excelente

calificacion = input("Por favor introduzca una califiación")
    














    
















                



