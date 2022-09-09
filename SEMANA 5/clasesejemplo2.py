class Persona:
    def __init__(self,nombre,apellidos,dni,correo,telefono):
        self.nombre= nombre
        self.apellidos= apellidos
        self.dni= dni
        self.correo= correo
        self.telefono= telefono
    def __str__(self):
        return self.nombre+" "+self.apellidos+" "+self.dni+" "+self.correo+" "+self.telefono
class Empleados(Persona):
    def __init__(self, nombre, apellidos, dni, correo, telefono,salario):
        super().__init__(nombre,apellidos,dni,correo,telefono)
        self.salario=salario
class Cliente(Persona):
    def __init__(self, nombre, apellidos, dni, correo, telefono,categoria):
        super().__init__(nombre,apellidos,dni,correo,telefono)
        self.categoria=categoria


personas=[]
def cargar():
    respuesta = input("a)Cliete o b)empleado:")
    if respuesta=='a':
        nombre = input("ingresa nombre:")
        apellidos = input("ingresa apellidos:")
        dni = input("ingresa dni:")
        correo = input("ingresa correo:")
        telefono = input("ingresa telefono:")
        salario = input("ingresa salario:")
        emp=Empleados(nombre,apellidos,dni,correo,telefono,salario)
        personas.append(emp)
    elif respuesta=='b':
        nombre = input("ingresa nombre:")
        apellidos = input("ingresa apellidos:")
        dni = input("ingresa dni:")
        correo = input("ingresa correo:")
        telefono = input("ingresa telefono:")
        categoria = input("ingresa categoria:")
        cli = Cliente(nombre, apellidos, dni, correo, telefono, categoria)
        personas.append(cli)

cargar()

for persona in personas:
    print(persona)