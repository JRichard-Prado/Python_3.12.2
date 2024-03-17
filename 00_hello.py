#comentario en una linea

print ("Hola Python 3.12.2")

"""otro comentario
en varias lineas
"""

print('Hola python') #String en comillas simples
print(''' Hola tres comillas''') #String en comillas triples
print(type("hola type")) # devuelve el tipo de la variable
print(type(True))
print(type({1.2, 1.2, "sdf "}))
##############Definicion de variables###############
""" 
Las variables son de tipo dimanico cambian automaticamente de acuerdo al valor asignado
"""
semanas=4
nom_mama= "Gaby"
nom_papa= "Richard"
texto=" y "
peso=65.2
# Formateo de string 
print("en {} semanas hay {} dias".format(semanas,7*semanas)  )
print("en %d semanas hay %d dias" %(semanas,7*semanas))
print(f"en {semanas} semanas hay {7*semanas} dias")
#Impresion sin salto de linea
print(f"{nom_mama} pregunta 'como estas??? '",end='dentro de '+str(semanas)+" semanas....... ")
print(f"{nom_papa} contesta \"muy bien gracias\"")# comillas dobles dentro de comillas dobles con \
print('un tipo pregunta "como estas?..."',end=" ")
print('el otro contesta \' not bat\'')
#Impresion sin salto de linea concatenado con un texto
print("'Hola'",end=texto)
print("\"Adios\"")
print(nom_mama,end=texto)
print(nom_papa)

print(f"Tu nombre es {nom_mama} y pesas {peso} kg")
print("Me llamo {} y mi peso es {} kg ...".format(nom_papa,peso))
print("Hola soy %s un gusto de saludarte %s tu peso aproximado es %d".capitalize() %(nom_mama.lower(),nom_mama.upper(),peso*2))