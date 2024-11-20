##Autor Jaime Ramon
# Solicitar al usuario que ingrese un texto
texto = input("Ingrese un texto de maximo 10 caracteres: ")

# Solicitar al usuario que ingrese la letra a buscar
letra = input("Ingrese la letra a buscar: ")

# Asegurarse de que el usuario solo introduzca una letra
if len(letra) != 1:
    print("Por favor, introduce solo una letra.")
else:
    contador = 0
    longitud = len(texto)

    # Verificar cada posición del texto 
    if longitud > 0 and texto[0] == letra:
        contador += 1
    if longitud > 1 and texto[1] == letra:
        contador += 1
    if longitud > 2 and texto[2] == letra:
        contador += 1
    if longitud > 3 and texto[3] == letra:
        contador += 1
    if longitud > 4 and texto[4] == letra:
        contador += 1
    if longitud > 5 and texto[5] == letra:
        contador += 1
    if longitud > 6 and texto[6] == letra:
        contador += 1
    if longitud > 7 and texto[7] == letra:
        contador += 1
    if longitud > 8 and texto[8] == letra:
        contador += 1
    if longitud > 9 and texto[9] == letra:
        contador += 1
    if longitud > 10 and texto[10] == letra:
        contador += 1


    print(f"La letra '{letra}' aparece {contador} veces en el texto.")

