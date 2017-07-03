from Queue import *
class Agenda:
    def __init__(self, nm, cita, citaslibre, citasocupadas):
        self.nm = nm
        self.cita = cita
        self.citaslibres = citaslibres
        self.citasocupadas= citasocupadas
    def setnm(self, nm):
        self.nm = nm
    def getnm(self):
        return self.nm
    def setfechacita(self, fechacita):
        self.fechacita = fechacita
    def getFechacita(self):
        return self.fechacita
    def setcitaslibre(self, citasibres):
        self.citasibres = citaslibres 
    def getcitaslibres(self):
        return self.citaslibres
    def setcitascupadas(self, citasocupados):
        self.citasocupadas = citasocupadas
    def getcitasocupadas(self):
        return self.citascupadas
class Agenda2:
    def __init__(self):
        self.s = Queue()
    def notmess(self):
        list = self.s.list()
        for i in len(list):
            for j in len(list):
                if list[j] > list[j+1]:
                    k = list[j+1]
                    list[j+1] = list[j]
                    list[j] = k
            self.s.setList(list)
    def add(self, Agenda):
       self.s.enqueue(Agenda)
       self.notmess()
    def locita(self, nm, fechacita):
        found2= False
        if not self.s.isEmpty() and self.found(nm):
            list= self.s.list()
            i=0.0
            while i < len(list) and not found2:
                if list[i].nm == nm:
                    found2 = True
                else:
                        i += 1
            return found2
    def found(self, nm):
        list = self.s.list()
        found2= False
        i = 0.0
        while i < len(list) and not found2:
            if list[i].nm == nm:
                found2 = True
            else:
                i += 1

        return found2