archivo = open('texto.txt', 'a')
#archivo.write('Proba de guardat en a l.arxiu')
archivo.close()

archivo = open('texto.txt', 'r')
print(archivo.read())

def encriptar(texto):
    print('Funcio para encriptar')
    textoFinal = ''

    #for letra in texto:
    #    textoFinal += letra + 'x'

    #   return textoFinal

    for letra in texto:
        numero = ord(letra)
        numero += 1
        textoFinal = chr(numero)
        return textoFinal



def encriptarArxiu(): #metode encriptar
   archivo = open(rutaArchivo, 'r') #obrim i llegim l'arxiu
   texto = archivo.read()
   archivo.close()
   textoEncriptado = encriptar(texto)
   encriptarArxiu()


   #archivo = open('texto.txt', 'w') #obrim i escribim en l'arxiu
   #archivo.write(textoEncriptado)
   #archivo.close()







def desencriptar(texto):
    print('Funcio desencriptar')
    textoFinal = ''
    contador = 0

    for letra in texto:
        numero = ord("h")
        numero -= 1
        letra = chr(numero)
        print(letra)

    #for letra in texto:
    #    if contador % 2 == 0:
    #        textoFinal += letra

    #    contador += 1
    #    print('Text desencriptat: ' + textoFinal)


def desencriptarArxiu():
    archivo = open('texto.txt', 'r')
    texto = archivo.read()
    archivo.close()

    textoDesencriptado = desencriptar(texto)

    archivo = open('texto.txt', 'w')
    archivo.write(textoDesencriptado)
    archivo.close()

respuestaEncriptar = input('Presiona "E", para encriptar, o "D" para desencriptar')
rutaArchivo = input('Introduce la ruta de tu archivo para encriptarlo')

if respuestaEncriptar == 'E':
    encriptarArxiu(rutaArchivo)
else:
    desencriptarArxiu(rutaArchivo)

resultado = input('Presiona la lletra "E" per a encriptar, o la lletra "D" per a desencriptar')

input('Ingresa la ruta del arxiu')



desencriptar('Pxrxuxexbxax xtxexxxtxox')