texto = "Hola gent"

#Recorrer text
for letra in texto:
    print('Lletra: ' + letra) #Printeja les lletres per iteracions del bucle


#Recorrer numeros
for numero in range(10): #Printejar fins al rang 10
    if numero > 5:
        print(numero)

#Diccionari
diccionari = {
    'Programar':"Programar es transformar el cafè en codi",
    'POO':'Programació orientada a objectes',
    'MVC':'Model vista controlador'
}

print(diccionari['POO']) #Accedeix dintre del valor que es troba al diccionari

diccionari2 = {
'0':'cero',
'1':'uno',
'2':'dos',
'3':'tres',
'4':'cuatro',
'5':'cinco',
'6':'seis',
'7':'siete',
'8':'ocho',
'9':'nueve',
}

textoFinal = ''

texto = input('Introdueix un numero: ')
for letra in texto:
    textoFinal += diccionari2[letra]

print(textoFinal)

