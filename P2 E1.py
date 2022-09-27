def cuantas_letras(datos):
    total = 0
    for linea in datos:
        linea = linea.split()
        n = 0
        for palabra in linea:
            n = n + len(palabra)
        total=total+n
    return total
himno = ["Puro Chile","es tu cielo azulado","puras brisas","te cruzan tambien"]
w=cuantas_letras(himno)
print(f"Hay {w} letras")
