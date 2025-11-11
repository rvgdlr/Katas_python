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



 


