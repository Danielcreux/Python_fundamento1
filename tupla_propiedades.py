#la función len() acepta tuplas, y regresa el número de elementos
#contenidos dentro; l operador + puede unir tuplas (ya se ha mostrado
#esto antes) l operador * puede multiplicar las tuplas, así como las
#listas; os operadores in y not in funcionan de la misma manera que en
#las listas.


my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
