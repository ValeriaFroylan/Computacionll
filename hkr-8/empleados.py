from Stack import Stack
class Empleado:
    def __init__(self, numberemplo):
        Tareas = Stack()
        self.numberemplo = 0
        self.Tareas = Tareas
        self.NumTareas = len(self.Tareas)
    def __init__(self, numberemplo, Tareas):
        self.numberemplo = 0
        self.Tareas = Tareas
        self.NumTareas = len(self.Tareas)
    def setnumberemplo(self, codigo):
        self.numberemplo= numberemplo
    def getnumberemplo(self):
        return self.numberemplo
    def setTareas(self, tareas):
        self.Tareas = tareas
    def getTareas(self):
        return self.Tareas
    def getNumTareas(self):
        return self.Tareas
    def tarea2(self):
        self.Tareas.pop()
class Emplea2:
    def __init__(self):
        self.s = Stack()
    def addEmpleado(self, empleado):
        self.s.push(empleado)
    def addTarea(self, tarea):
        primero = 0
        ya = 0
        list = self.t.list()
        for i in list:
            if list[i].NumTareas < primero:
                ya = i
                menos = list[i].NumTareas
        list[ya].Tareas.push(tarea)
        if not self.s.isEmpty():
            self.s.items = []
        for i in list:
            self.s.push(list[i])
    def list(self):
        return list(self.s.items)
    def see(self, empleado):
        list = self.list
        found= False
        for i in list:
            if list[i].numberemplo == empleado:
                found = True
        return found
    def tarea2(self, empleado):
        list = self.list()
        for i in list:
            if list[i].numberemplo == empleado:
                list[i].Tareas.pop()
                break
class Tarea:
    def __init__(self, area, info):
        self.area = area
        self.info = info
    def __str__(self):
        return "Area: " + self.area + "Descripcion: " + self.info
    def setarea(self, area):
        self.area = area
    def getarea(self):
        return self.area
    def setinfo(self, info):
        self.info = info
        def getinfo(self):
            return self.info
class Tareas:
    def __init__(self):
        s = Stack()
    def __init__(self, tareas):
        self.s = tareas
    def addTarea(self, tarea):
        self.s.push(tarea)
    def elTarea(self):
        return self.s.pop()
    def Entero():
        while True:
            try:
                numero = int(raw_input())
            pass
        return numero
    def Flotante():
        while True:
            try:
                numero = float(raw_input())
            pass
        return numero
    def Char():
        while True:
            try:
                numero =char( raw_input())
            pass
        return numero[0]
    def Cadena():
        while True:
            try:
                numero = input()
            pass
        return numero
class Main:
    def main()
        contador= True
        empleados = Empleados()
        while contador:
            inico = "1.-Agregar empleado "
            inicio+= "2.-Agregar tarea"
            inicio += "3.-Tarea finalizada"
            inicio += "4.-Salir"
            respueta = Entero(inico)
            if respuesta == 1:
                numberemplo = Entero("Numero de empleado:")
                empleados.push(Empleado(numberemplo))
            elif respueta == 2:
                area = Cadena("Area del empleado:")
                info = Cadena("Descripcion: ")
                tarea = Tarea(area, info)
                empleados.addTarea(tarea)
            elif respuesta == 3:
                empleado = Cadena("empleado")
                if empleados.found(empleado):
                    empleados.tarea2(empleado)
            elif respuesta == 4:
                break
            else:

                print "No existe esa opción"