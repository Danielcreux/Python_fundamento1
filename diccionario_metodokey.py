#El método retorna o regresa una lista de todas las claves dentro del
#diccionario. Al tener una lista de claves se puede acceder a todo el
#diccionario de una manera fácil y útil

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

