archivo = open('texto.txt', 'a')
archivo.write('Proba de guardat en a l.arxiu')
archivo.close()

archivo = open('texto.txt', 'r')
print(archivo.read())

def encriptar(texto):
    print('Funcio para encriptar')
    textoFinal = ''

    for letra in texto:
        textoFinal += letra + 'x'

        return textoFinal



def encriptarArxiu(): #metode encriptar
   archivo = open('texto.txt', 'r') #obrim i llegim l'arxiu
   texto = archivo.read()
   archivo.close()
   textoEncriptado = encriptar(texto)

   archivo = open('texto.txt', 'w') #obrim i escribim en l'arxiu
   archivo.write(textoEncriptado)
   archivo.close()

encriptarArxiu()

def desencriptar(texto):
    print('Funcio desencriptar')
    textoFinal = ''
    contador = 0

    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra

        contador += 1
        print('Text desencriptat: ' + textoFinal)

def desencriptarArxiu():
    archivo = open('texto.txt', 'r')
    texto = archivo.read()
    archivo.close()

    textoDesencriptado = desencriptar(texto)

    archivo = open('texto.txt', 'w')
    archivo.write(textoDesencriptado)
    archivo.close()

resultado = input('Presiona la lletra "E" per a encriptar, o la lletra "D" per a desencriptar')

input('Ingresa la ruta del arxiu')

if


desencriptar('Pxrxuxexbxax xtxexxxtxox')