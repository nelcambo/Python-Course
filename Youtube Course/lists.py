l = [2, "tres", True, ["uno", 10]]
#print (l " es una lista") : no funciona ya que uno es una lsita y el otro un string
print ("{0} es una lista".format(l))
# eso es una lista, que en la posicion 4 (Indice 3) posee tambien una lista 
print (l[1])
# Esto nos devolvera la entrada en el indice 1, que es la posicion 2, osea, "tres"
# Tambien podemos almacenar esta informacion en otra variable
l2 = l[1]
print (l2)

print("Ahora accederemos a uno de los elementos en la lista dentro de la lista, el uno ") 
print ("Ese esta en el indice 3 de la primera lista y en el indice 0 de la segunda lista") 

print(l[3][0]) 

# Aca podemos tambien redefinir valores dentro de la lsita e incluso tipo de estructura de datos

l[1] = 4
print (l)
# En este caso aparecera la lista actualizada

# Si solo quisieramos tomar algunos valores de la lista, como un rango, podemos hacerlo asi: 

l3 = l[0:3] # lo cual nos devuelve solo los indices 0, 1 y 2 y NO  EL 3
# [2, 4, True]
print (l3)

# Ahora bien, si deseamos tomar datos alternantes de la lista (uno si y uno no)
# Agregamos un segundo : a la instruccion con valor n+1 de la alternancia 
# por ejemplo si es uno si y uno no, debemos poner salto 2, tiene sentido, pues True esta a dos posiciones del 2

l3 = l[0:3:2]
print (l3)
# Podriamos omitir el indice superior  y solo colocar l3 = l[0::2]
# Lo cual retornaria la lista completa intercalada de uno en uno
l3 = l[0::2]
print (l3)
# En este caso, se salta uno y ya no hay mas elementos en la lista para mostrar, por eso queda igual
# Editemos la lista para verlo mejor 
l = [2, "tres", True, ["uno", 10], [False, 2.3]]
print("Nueva lista")
print(l)
l3 = l[0::2]
print (l3)
# Podemos tambien perfectamente empezar en otro punto, como el indice 1

l = [2, "tres", True, ["uno", 10], [False, 2.3]]
print(l) 
l3 = l[1::2]
print (l3)

#Podemos tambien editar secciones enteras de una lista
# Vamos a cambiar los dos primeros elementos de la lista
print(l) 
print("Es la lista original, cambiaremos los dos primeros elementos")
l[0:2] = ["cuatro", 3]
print("La nueva lista es:") 
print(l)
# Mostrando ahora ['cuatro', 3, True, ['uno', 10], [False, 2.3]] 
