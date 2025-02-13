def contar_vocale_letras():  # definir función
    frase = input("Ingresa una frase: ")  # solicitar al usuario una frase

    vocales = "aeiouáéíóú"  # definir las vocales
    contador_letras = 0  # inicializar contador de letras
    contador_vocales = 0  # inicializar contador de vocales

    for caracter in frase.lower():  # recorrer cada carácter en la frase
        if caracter.isalpha():  # verificar si el carácter es una letra
            contador_letras += 1  # incrementar el contador de letras
            if caracter in vocales:  # si es una vocal, incrementar el contador de vocales
                contador_vocales += 1

    # Mostrar los resultados fuera del bucle para evitar repeticiones
    print(f"Cantidad de letras: {contador_letras}")
    print(f"Cantidad de vocales: {contador_vocales}")


contar_vocale_letras()  # llamar la función
        