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






