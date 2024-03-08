a = 4#int(input("valor entero de a: "))
#print(type(a))
b= 2#int(input("valor entero de b: "))
print("resultado del la suma es: " + str(a+b)) #no podemos concatenar numeros directamente con +


print("resultado del la multiplicacion es: " + str(a*b))
print("resultado del la division es: " + str(a/b))
print("resultado del la resta es: " + str(a-b))
print("resultado del la division con redondeo hacia abajo es: " + str(a//b))

edad = 43 #int(input('Teclear edad: '))  # entrada de entero
peso = 65.2 #float(input('Teclear peso: '))  # entrada de flotante
nombre = "gaby" #input('Teclear nombre: ')  # entrada de cadena
print(nombre, edad,'años', peso,'kg') #concatenados
print("{} {} años {} kg".format(nombre,edad,peso)) # muestra datos formateados
print(type(edad))
print(type(peso))
print(type(nombre))
#operadores condicionales
print(edad <= peso)
print(edad >= peso)
print(edad == peso)
print(edad != peso)
n=37
print(bin(n))
print(int.bit_length(37))
