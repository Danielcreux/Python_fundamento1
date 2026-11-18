blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
height = 0
blocks_needed = 1

while blocks >= blocks_needed:
    blocks = blocks - blocks_needed
    height = height + 1
    blocks_needed = blocks_needed + 1

print("La altura de la pirámide:", height)

