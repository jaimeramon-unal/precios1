##Autor Jaime Ramon
# Solicitar al usuario que ingrese una cadena
palabra = input("Introduce una cadena: ")

es_todo_letra = True

# Evaluar carácter por carácter de forma manual
if len(palabra) > 0:
    if not ('a' <= palabra[0] <= 'z' or 'A' <= palabra[0] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 1:
    if not ('a' <= palabra[1] <= 'z' or 'A' <= palabra[1] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 2:
    if not ('a' <= palabra[2] <= 'z' or 'A' <= palabra[2] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 3:
    if not ('a' <= palabra[3] <= 'z' or 'A' <= palabra[3] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 4:
    if not ('a' <= palabra[4] <= 'z' or 'A' <= palabra[4] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 5 :
    if not ('a' <= palabra[5] <= 'z' or 'A' <= palabra[5] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 6:
    if not ('a' <= palabra[6] <= 'z' or 'A' <= palabra[6] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 7:
    if not ('a' <= palabra[7] <= 'z' or 'A' <= palabra[7] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 8:
    if not ('a' <= palabra[8] <= 'z' or 'A' <= palabra[8] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 9:
    if not ('a' <= palabra[9] <= 'z' or 'A' <= palabra[9] <= 'Z'):
        es_todo_letra = False
if len(palabra) > 10:
    if not ('a' <= palabra[10] <= 'z' or 'A' <= palabra[10] <= 'Z'):
        es_todo_letra = False


# Mostrar el resultado
if es_todo_letra:
    print("Todos los símbolos son letras.")
else:
    print("No todos los símbolos son letras.")