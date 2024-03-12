#------------ Tipos Variables Pyhton---------------

nom_hijo = "juan Pablo" #convencion de nombre de variable snek_keys
nom_papa = "Juan Richard"
edad_hijo = 5
edad_papa=43
sexo = "masculino"

# tipo de datos enteros definidos en una sola linea
year,dia, edad_papa,temperatura, angulo = 2024,7,43, 16, 45

#tipo dato floatttt
pi =3.1416
estatura= 1.65
peso=65.4
temperatura= 35.6
distancia_linea1 =26.5
#tipo datos boolean
esta_frio = True
es_alto = False
#listas o datos compuestos
equares_lista =[1**2,2**2,3**2,4**2,5**2,6**2]
cubes =[1**3,4**3,3**3]

#input ingresar por consola teclado
#papa, mama, hijo, añospablo =input( "nombre papa"), input("nombre mama"), input("Juan Pablo??"), 5
#print(nom_hijo)
"""
cual es la suma de las edades de papa y el hijo??
comentarios en varias lineas
"""
#print(len(nom_hijo))
"""
edad_hijo=int(input("ingresar edad de hijo"))
edad_papa=int(input("ingesar edad papa"))"""

print( f"la edad de {nom_hijo[0:5]} es {edad_hijo} \ny la edad de {nom_papa} es {edad_papa} \ny la suma de las edades es {edad_hijo + edad_papa} ",)
print( rf"la edad de {nom_hijo} es {edad_hijo} \ny la edad de {nom_papa} es {edad_papa} \ny la suma de las edades es {edad_hijo + edad_papa} ",)
#concatenacion de variables en un print
print(edad_hijo, edad_papa)
print("c: usr\nombres")
print(r"C: usr\nombres\hello word")
print(2*f"""hola {nom_hijo[-5:]}
      como estas print en varias            lineas
            un gusto de                     saludarte {nom_papa[5:12]}\n""")
print('hola ' 'juan pablo sin comas')
print("la ptencia de 2 elevado a la 3 es ", end="=")
print(2**3)
print(pow(2,edad_hijo))
print(nom_hijo[0:5])
print(nom_hijo[-10:-6])
print(nom_hijo[5:])# contar de isquierda
print(nom_hijo[-5:])
print(nom_papa[5:])
print(str.lower(nom_hijo))
print(nom_hijo.title())
print(nom_papa.swapcase())
print(nom_hijo.upper())
print(nom_papa.isalpha())
print(sexo.isalpha())
print(len("luisagabylaimevillarroel"))
print("luisa gaby laime villarroel".upper())
print("luisa gaby laime villarroel".lower())
print("luisa gaby laime villarroel".capitalize())
print("luisa gaby laime villarroel".title())
print("luisa gaby laime villarroel ".swapcase()*2)
print(equares_lista[:])
print(equares_lista[0])
print(equares_lista[-1])
equares_lista.append(7**3)
equares_lista.append(8**3)
print(equares_lista)
print(cubes)
print(sorted(cubes*5)) #listas ordenados 


