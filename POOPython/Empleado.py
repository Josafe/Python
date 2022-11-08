class Persona:
    def __init__(self, nombre, apellido, dni, telefono):
        self. nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

class Empleado(Persona): #Hereda tots els atributs de persona
    def __init__(self, nombre, apellido, dni, telefono, salario):
        super().__init__(nombre, apellido, dni, telefono)
        self.salario = salario

class Cliente: #Aquesta hereda tots els atributs de persona i a part li afegi un camp nou
    def __init__(self, nombre, apellido, dni, telefono, correo):
        super().__init__(nombre, apellido, dni, telefono)
        self.correo = correo


emp = Empleado('Lucas', 'Zubeldia', '496334123B', '612781994')
cli = Cliente('Lucas', 'Zubeldia', '496334123B', '612781994', 'lukyz@gmail.com')


def cargar():
    respuesta = input('Quieres agregar un empleado?')
    nombre = input('Ingresa el nombre')
    apellido = input('Introduce el apellido')
    dni = input('Introduce su DNI')
    telefono = input('Introduce su telefono')

    if (respuesta == 'si'):

        salario = input('Introduce su salario')
        emp = Empleado(nombre, apellido, dni, telefono, int(salario)) #Introduirem els parametres manualment si activem el metode cargar, al ser un empleat també disposara de un salari el qual esta amb una variable interna

    else:
        tipo = input('Ingrese el tipo de cliente')
        cli = Cliente(nombre, apellido, dni, telefono, tipo) #Introduirem els parametres manualment si activem el metode cargar.

print(Empleado)
print(Cliente)