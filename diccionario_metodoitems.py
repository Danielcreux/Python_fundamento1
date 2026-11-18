#Este método retorna una lista de tuplas (este es el primer ejemplo en
#el ue las tuplas son mas que un ejemplo de si mismas) donde cada tupla
#es n par de cada clave con su valor

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)

