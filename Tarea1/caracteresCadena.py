##Autor Jaime Ramon
# Solicitar al usuario que ingrese una palabra
palabra = input("Introduce una palabra: ")

# Contador de consonantes
contador_consonantes = 0

if len(palabra) > 0:
    if palabra[0].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 1:
    if palabra[1].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 2:
    if palabra[2].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 3:
    if palabra[3].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 4:
    if palabra[4].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 5:
    if palabra[5].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 6:
    if palabra[6].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 7:
    if palabra[7].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 8:
    if palabra[8].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 9:
    if palabra[9].lower() not in 'aeiou':
        contador_consonantes += 1
if len(palabra) > 10:
    if palabra[10].lower() not in 'aeiou':
        contador_consonantes += 1

# Mostrar el resultado
print(f"La cadena contiene {contador_consonantes} consonantes")