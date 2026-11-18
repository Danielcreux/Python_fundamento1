word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ").upper()
# y asignarla a la variable user_word.


for letra in user_word:
    # Completa el cuerpo del bucle.
    for letra in user_word:
        if letra == "A":
            continue
        elif letra == "E":
            continue
        elif letra == "I":
            continue
        elif letra == "O":
            continue
        elif letra == "U":
            continue
        else:
            word_without_vowels = word_without_vowels + letra
# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)



