def cadena_frecuencias(texto):
    frecuencias = {}
    for letra in texto:
        if letra !="":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias






