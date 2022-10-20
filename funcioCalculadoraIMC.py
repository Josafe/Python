#def calcularIMC(parametro1, parametro2):


def calcularIMC(peso, alturametro):
    imc = peso / (alturametro * alturametro)
    return imc


def pedirIMC():
    peso = float(input("Ingresa el teu pes en kg"))
    altura = int(input("Ingresa la teva altura en cm"))
    alturametro = altura / 100
    imc = calcularIMC(peso, alturametro)

    if (imc < 19):
        input("Tens infrapes, IMC de:" + str(imc))
    
    if (imc >= 20 and imc <= 25):
        input("Tens el pes normal, IMC de:" + str(imc))

    if (imc > 25 and imc <= 30):
        input("Tens sobrepes, IMC de:" + str(imc))

    if (imc > 30):
        input("Tens obesitat, IMC de:" + str(imc))



print("Primera persona")
#calcularIMC('95', '187')
pedirIMC()

print("Segona persona")
#calcularIMC('86', '187')

print("Tercera persona")
#calcularIMC('71.5', '170')

