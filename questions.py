import random

categorias = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "animales": ["perro", "gato", "elefante", "jirafa", "tigre", "conejo", "caballo", "delfin"],
    "frutas": ["manzana", "banana", "naranja", "frutilla", "melon", "durazno", "pera", "uva"],
}

print("Categorías disponibles:")
for cat in categorias.keys():
    print(f"  - {cat}")

eleccion = input("Elegí una categoría: ").strip().lower()
if eleccion not in categorias:
    print("Categoría no válida, se usa 'programacion' por defecto.")
    eleccion = "programacion"

words = categorias[eleccion]
word = random.choice(words)
guessed = []
attempts = 6
incorrectas = 0
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    if "_" not in progress:
        print("¡Ganaste!")
        puntaje = 6 - incorrectas
        print(f"Puntaje: {puntaje}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")

    if len(letter) != 1 or not letter.isalpha():
        print("Entrada no válida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        incorrectas += 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    print("Puntaje: 0")