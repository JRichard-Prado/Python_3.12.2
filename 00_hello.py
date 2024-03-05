#esto es un comentario en una linea

print ("hola Python 3.12.2")

"""otro comentario
en varias lineas
"""

print('hola python') #string en comillas simples
print(''' hola tres comillas''') #estring en comillas triples
print(type("hola type")) # devuelve el tipo de la variable
print(type(True))
print(type({1.2, 1.2, "sdf "}))
"""Definicion de variables 
las variables son de tipo dimanico cambian automaticamente de acuerdo al valor asignado
"""
semanas=4
nom_mama= "Gaby"
nom_papa= "Richard"
texto=" y "
peso=65.2
# formateo de string 
print("en {} semanas hay {} dias".format(semanas,7*semanas)  )
print("en %d semanas hay %d dias" %(semanas,7*semanas))
print(f"en {semanas} semanas hay {7*semanas} dias")
#impresion sin salto de linea
print(f"{nom_mama} pregunta 'como estas??? '",end='dentro de '+str(semanas)+" semanas....... ")
print(f"{nom_papa} contesta \"muy bien gracias\"")# comillas dobles dentro de comillas dobles
print('un tipo pregunta "como estas?..."',end=" ")
print('el otro contesta \' not bat\'')
#impresion sin salto de linea concatenado con un texto
print("'Hola'",end=texto)
print("\"Adios\"")
print(nom_mama,end=texto)
print(nom_papa)

print(f"tu nombre es {nom_mama} y pesas {peso} kg")
print("me llamo {} y mi peso es {} kg ...".format(nom_papa,peso))
print("hola soy %s un gusto de saludarte %s tu peso aproximado es %d".capitalize() %(nom_mama.lower(),nom_mama.upper(),peso*2))