import random

def obtener_palabra_secreta():
    palabras = ['python', 'programacion', 'computadora', 'inteligencia', 'artificial', 'codigo']
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += '_'
    return progreso

def pedir_letra():
    letra = input("Ingrese una letra: ").lower()
    return letra

def chequear_letra(letra, palabra_secreta):
    return letra in palabra_secreta

def jugar():
    vidas = 6
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []

    while vidas > 0:
        print("\nVidas restantes:", vidas)
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print("Progreso:", progreso_actual)

        letra = pedir_letra()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingrese una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has ingresado esta letra antes.")
            continue

        letras_adivinadas.append(letra)

        if chequear_letra(letra, palabra_secreta):
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("La letra no está en la palabra.")
            vidas -= 1

        if '_' not in mostrar_progreso(palabra_secreta, letras_adivinadas):
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

    if vidas == 0:
        print("¡Has perdido! La palabra era:", palabra_secreta)

jugar()
