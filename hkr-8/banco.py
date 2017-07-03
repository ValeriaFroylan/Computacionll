import Stack
class Banco:
    def __init__(self):
        self.s1 = Stack()
    def __str__(self):
        return self.s1.items
    def list(self):
        return self.s1.list()
    def saldo(self, cuenta):
        list = self.list()
        saldofinal = 0
        for i in list:
            if list[i].cuenta == cuenta:
                if list[i].tipo in "primer tipo":
                    saldofinal += list[i].saldo
                if list[i].tipo == "segundo tipo":
                    saldofinal -= list[i].saldo
            return saldofinal
    def depo(self, primero, segundo):
        list = self.list()
        depo = 0
        a1 = 0
        for i in list:
            if list[i].tipo in "primer tipo" and list[i].fecha >= primero and list[i].fecha <= segundo:
                a1 += 1
                depo += list[i].saldo
        return "Cantidad de depositos: " + a1 + "Cantidad: " + depo
    def retiros(self, primero, segundo):
        list = self.list()
        retiros = 0
        a1 = 0
        for i in list:
            if list[i].tipo in "segundo tipo" and list[i].fecha >= primero and list[i].fecha <= segundo:
                a1 += 1
                retiros -= list[i].saldo
        return "Cantidad de retiros: ",a1,"Cantidad: ",retiros
    def move(self, movimiento):
        self.s1.push(movimiento)
    def a2Stack(self, list):
        if not self.s1.isEmpty():
            self.s1.items = []
        for i in list:
                self.s1.push(list[i])
class Movimiento:
    def __init__(self, id, cuenta, fecha, saldo, tipo):
        self.id = id
        self.cuenta = cuenta
        self. fecha = fecha
        self.saldo = saldo
        self.tipo = tipo
    def SetId(self, id):
        self.id = id
    def GetId(self):
        return self.id
    def setCuenta(self, cuenta):
        self.cuenta = cuenta
    def getCuenta(self):
        return self.id
    def setFecha(self, fecha):
        self.fecha = fecha
    def getFecha(self):
        return self.fecha
    def setSaldo(self, saldo):
        self.saldo = saldo
    def getSaldo(self):
        return self.saldo
    def setTipo(self, tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def __str__(self):
        informacion = "Id: " + self.id + ", Fecha: " + self.fecha + ", saldo: " + self.saldo + ", Tipo: " + self.tipo
        return informacion
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
    def main():
        contador = True
        banco = Banco()
        while contador:
            inicio = "1.-Agregar Movimiento\a1"
            inicio += "2.-Saldo de cuenta\a1"
            inicio += "3.-Depositos\a1"
            inicio += "4.-Retiros\a1"
            inicio += "5.-Salir\a1"
            respuesta = Entero("Digite su respuesta\a1")
            if respueta == 1:
                id = Entero("Digite el id")
                cuenta = Entero("Digite el Numero de cuneta")
                fecha = Entero("Digite la fecha")
                saldo = Entero("Digite ls cantidad de dinero")
                tipo = Char("Digite el tipo de cuenta")
                movimiento = Movimiento(id, cuenta, fecha, saldo, tipo)
                banco.move(movimiento)
            if respuesta == 2:
                a2Cuenta = Entero("digite un numero de cuenta")
                print banco.saldo(a2Cuenta)
            if respuesta == 3:
                primero = Entero("Diga maxima fecha")
                segundo = Entero("Diga minima fecha")
                if segundo < primero :
                    print "No hay resultado para esta busqueda"
                else:
                    print banco.retiros(primero, segundo)
            if respuesta == 4:
                primero = Entero("Diga maxima fecha")
                segundo = Entero("Diga maxima fecha")
                if segundo < primero :
                    print "No hay resultado para esta busqueda"
                else:
                    print banco.depo(primero, segundo)
            if respuesta == 5:
                contador = False