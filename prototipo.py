import random

# Base de datos básica con palabras y pistas
PALABRAS = [
    {"palabra": "PROGRAMACION", "pista": "Escribir código e instrucciones para computadoras."},
    {"palabra": "PYTHON", "pista": "Un lenguaje de programación muy popular y fácil de aprender."},
    {"palabra": "ELEFANTE", "pista": "El mamífero terrestre más grande del mundo."},
    {"palabra": "COLOMBIA", "pista": "País sudamericano famoso por su café."},
    {"palabra": "ALGORITMO", "pista": "Pasos ordenados para resolver un problema."}
]

# Arte ASCII básico para el ahorcado
DIBUJOS_AHORCADO = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

def jugar_ahorcado():
    # Seleccionar una palabra al azar
    item_seleccionado = random.choice(PALABRAS)
    palabra_secreta = item_seleccionado["palabra"]
    pista = item_seleccionado["pista"]
    
    letras_adivinadas = set()
    intentos_fallidos = 0
    max_intentos = 6

    print("========================================")
    print("      ¡JUEGO DEL AHORCADO EN PYTHON!     ")
    print("========================================\n")

    while intentos_fallidos < max_intentos:
        # Mostrar el dibujo del ahorcado según los fallos
        print(DIBUJOS_AHORCADO[intentos_fallidos])
        print(f"\nPISTA: {pista}")
        
        # Mostrar la palabra oculta con guiones bajos o letras descubiertas
        palabra_mostrada = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print("\nPalabra: " + " ".join(palabra_mostrada))
        print(f"Intentos restantes: {max_intentos - intentos_fallidos}")
        
        if letras_adivinadas:
            print("Letras probadas: " + ", ".join(sorted(letras_adivinadas)))
        
        # Comprobar si ya adivinó toda la palabra
        if "_" not in palabra_mostrada:
            print("\n----------------------------------------")
            print(f"¡FELICIDADES! ¡Adivinaste la palabra: {palabra_secreta}!")
            print("----------------------------------------")
            break

        # Pedir letra al usuario
        letra_usuario = input("\nIngresa una letra: ").strip().upper()

        # Validaciones de la entrada
        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print(">> Por favor, ingresa solo una letra válida.")
            continue

        if letra_usuario in letras_adivinadas:
            print(">> Ya ingresaste esa letra anteriormente. Intenta con otra.")
            continue

        # Registrar la letra ingresada
        letras_adivinadas.add(letra_usuario)

        # Evaluar si la letra está en la palabra secreta
        if letra_usuario in palabra_secreta:
            print(f">> ¡Bien hecho! La letra '{letra_usuario}' está en la palabra.")
        else:
            intentos_fallidos += 1
            print(f">> La letra '{letra_usuario}' NO está en la palabra.")

    # Si se agotan los intentos y no ganó
    if intentos_fallidos == max_intentos:
        print(DIBUJOS_AHORCADO[intentos_fallidos])
        print("\n----------------------------------------")
        print(f"¡GAME OVER! Has quedado ahorcado.")
        print(f"La palabra secreta era: {palabra_secreta}")
        print("----------------------------------------")

if __name__ == "__main__":
    jugar_ahorcado()