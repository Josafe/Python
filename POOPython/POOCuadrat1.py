class Cuadrado:
    def __init__(self, an, al): #Constructor, es sol ficar el mateix nom per a no complicarse tant però aixi es veu que s'agafen variables diferents.
        self.ancho = an
        self.alto = al

    def calcularArea(self):
        area = ancho * alto
        return area


figura = Cuadrado(10, 12)

print(figura.ancho) #Accedim a les dades internes de l'objecte.
print(figura.calcularArea()) #Accedim dintre de la funció calcularArea