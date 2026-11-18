#Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

while True:
    palabra = input("Ingrese una palabra:")
    
    if palabra == "chupacabra":
       break
print("Has dejado el bucle con éxito")