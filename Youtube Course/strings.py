myStr = "hello world"

print(myStr)

#print(dir(myStr))
#arroja todas las opciones que se tienen para hacer o ejecutar con el string
# print(myStr.upper())
# # Escribe todo el string en Mayusculas 
# print(myStr.lower())
# # Escribe todo el string en minusculas 
# print(myStr.swapcase())
# # Intercambia las mayusculas y minusculas originales 
# print(myStr.capitalize())
# # Tambien escribe todo el string en Mayusculas
# print(myStr.replace('hello', 'bye'))
# # Reemplaza parte del string, en este caso hello por bye retornando: bye world
# print(myStr.count(' '))
# # Cuenta la cantidad de caracteres en blanco en el string (en este caso retorna 1)
# print(myStr.count('o'))
# # Cuenta la cantidad de caracteres "o" en el string (en este caso retorna 2)
# print(myStr.count('l'))
# # Cuenta la cantidad de caracteres "l" en el string (en este caso retorna 3)
# print(myStr.startswith('he'))
# # Retorna un verdadero o falso de si el string comienza por "he", en este caso retorna un "true"
# print(myStr.endswith('world')) 
# # Retorna un verdadero o falso de si el string finaliza en "world", en este caso retorna un "true"
# print(myStr.split('o')) 
# # Divide el string alrededor del "o", retornando la lista ['hell', ' w', 'rld'] con 3 entradas
# print(myStr.find('z')) 
# # Retorna la ubicacion del caracter "z" en el string, en este caso no lo hay, por lo cual retorna como -1
# print(myStr.find('d'))
# # Retorna la ubicacion del caracter "d" en el string, en este caso la posicion 10
# # ya que se empieza contando desde la posición "0" y no desde "1"
# print(len(myStr))
# # Nos retorna la longitud total de caracteres en el string, que son 11. 
# print(myStr.index('e'))
# # Retorna la ubicacion del caracter "e" en el string, en este caso la posicion 1
# # que es la segunda ya que contamos desde el "0"
# print(myStr.isnumeric())
# # Consulta si el string es numerico o no, retorna false
# print(myStr.isalpha())
# Consulta si el string es alfanumerico o no, retorna false 
print(myStr[4])
# Retorna la posicion 5 del string (recordemos que cuenta desde cero), en este caso "o"
# ---------------------------------------------------------------------------------------- 
# Para no obtener todos estos resultados cada vez, podemos comentar todas las lineas anteriores 
# Seleccionamos las lineas y mediante Ctrl + Shift + P, seleccionamos "Add Line Comment"
# ----------------------------------------------------------------------------------------
print(myStr[0])
# Retorna la posicion 1 del string (recordemos que cuenta desde cero), en este caso "h"
print(myStr[1])
print(myStr[2])
print(myStr[3])
print(myStr[4])
print(myStr[5])
# Tambien podemos ir a la inversa ingresando posiciones negativas para que se invierta el sentido 
print(myStr[-1])
print(myStr[-2]) 
print(myStr[-3])
print(myStr[-4]) 
print(myStr[-5])
# Definamos un nuevo string myNewStr = Nelson
myNewStr = "Nelson"
print ("My name is " + myNewStr)
print (f"My name is {myNewStr}") # Solo disponible de la version 3.6 hacia arriba
# Los resultados en pantalla son los mismos, la diferencia la hace la "f" inicial
# y el hecho de que la variable se encuentra entre llaves
# otra forma seria: 
print ("My name is {0}".format(myNewStr))

# Aprendamos caracteres de escape
# /n es para nueva linea en el string 
# /t es para una tabulacion dentro del string
# Estos do caracteres de escape se pueden combinar 

cads = 'Texto entre \n comillas' 
cads2 = 'Texto entre \ncomillas'  # va sin espacio
cadd = "Texto entre \n\tcomillas dobles" 
print (cads ) 
print (cads2)
print (cadd) 

# Ahora, si usamos comillas triples, no hacen falta loss carqacteres de escape
# El editor respeta los saltos de linea que introducimos

cadc ="""Esto es un solo string de varias lineas 
linea 1
linea 2
linea 3
.
.
.
linea n 
fin del string"""

print(cadc)

# Repeticion y Concatenacion de strings 

cad = "Cadena" * 3
print (cad)
cad1 = "Cadena 1" 
cad_ = " y "
cad2 = "Cadena 2"
print(cad1 + cad_ + cad2)

# Tambien podemos almancenar la concatenacion en otra variable

cad3 = cad1 + cad_ + cad2 

print (cad3)


