
from lib2to3.pgen2.token import PLUS


#print('Dame dos numeros por favor')
#n1=input("Ingrese el primer numero: ")
#int(n1) # Pretende convertir a entero el string obtenido n1
#n2=input("Ingrese el segundo numero: ")
#int(n2) # Pretende convertir a entero el string obtenido n2 
# En un intento por sumar los numeros solo obtengo la concatenacion 
# de los dos numeros uno delante del otro
# debo saber como sumarlos e imprimir la suma
#print(n1 + n2) 
# Creo que puede ser este
#sum(n1,n2)
# Probemos a ver 
#print(sum(n1,n2))
# Falla
# Error: TypeError: sum() can't sum strings [use ''.join(seq) instead]
# n1 y n2 siguen siendo strings y no numeros
# creo que debe declararse al momento de pedir el input 
# acabo de descubrir que no se puede en https://www.youtube.com/watch?v=DRBybZ6hsY0 
# debo redefinir la variable como su entero n1=int(n1)
# /////////////////////////////////////////////////////////////////// 

print('Dame dos numeros por favor')
n1=input("Ingrese el primer numero: ")
n1=int(n1) # Conseguira convertir a entero el string obtenido n1
n2=input("Ingrese el segundo numero: ")
n2=int(n2) # Conseguira convertir a entero el string obtenido n2 
print(n1 + n2) 

# Acabo de aprender que tambien puedo declararla como entero al momento de tomar los datos 
# number = int(input('Introduzca un numero'))
number = int(input('Introduzca un numero: '))
print(type(number))