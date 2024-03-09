# cosntructor String 

primer_string = "string"
seg_string = "segundo string"

print(len(primer_string)) # cantidad de caracteres
print(primer_string +"\t"+ seg_string)  #concatenacion
#formateo
print("este es {} \t este el {}".format(primer_string,seg_string))
print(2*f"este es :{primer_string} \neste el: {seg_string}\n") #formateo con salto de linea

#desempaquetado  de la cadena String
a,s,d,f,q,w = primer_string
print(a, end="")
print(s, end="")
print(d,end="")
print(f,end="")
print(q,end="")
print(w)

#division de string

print(primer_string[-1])
print(primer_string[::-1])# reverce da la vuelta a la cadena
print(primer_string[1:3])
print(primer_string[:])
#funciones
print(primer_string.capitalize())
print('el indice donde se encuentra n es :',primer_string.index('n'))
print(primer_string.upper())
print(primer_string.count("t"))
print(primer_string.isnumeric())
print(primer_string.startswith("st"))
print(primer_string.upper().isupper())
#Alinear el texto y especificar el ancho:
print('{:*^50}'.format('centrado texto'))
print('{:*<50}'.format("texto a la isquierda"))
print('{:*>50}'.format('rigth aligned text'))
