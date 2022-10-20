seguirchateando = True

while seguirchateando:
    texto = input('>')

    if texto == 'salir':
        seguirchateando = False

    texto = texto.replace(':)', '😀')
    texto = texto.replace(':(', '😌')
    texto = texto.replace(':P', '😋')
    texto = texto.replace(':3', '😘')
    print(texto)