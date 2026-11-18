# Paso 1: crear una lista vacía
beatles = []

# Paso 2: agregar miembros con append()
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3: pedir al usuario dos miembros más usando for y append()
for i in range(2):
    miembro = input("Introduce un miembro de la banda: ")
    beatles.append(miembro)

# Paso 4: eliminar a Stu Sutcliffe y Pete Best
del beatles[3]
del beatles[3]

# Paso 5: agregar a Ringo Starr al principio
beatles.insert(0, "Ringo Starr")

print(beatles)
