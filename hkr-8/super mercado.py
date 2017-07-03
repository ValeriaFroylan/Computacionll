from Queue import *
class Producto:
    def __init__(self, numprod, hmuch, numR):
        self.numprod= numprod
        self.hmuch= hmuch
        self.numR = numR
    def setnumprod(self, numprod):
        self.numprod = numprod
    def getnumprd(self):
        return self.numprod
    def sethmuch(self, hmuch):
        self.hmuch = hmuch
        self.numR += 1
    def gethmuch(self):
        return self.hmuch
class MarkProd:
    def __init__(self):
        self.s = Queue()
    def notmess(self):
        list = self.s.list()
        for i in len(list):
            for j in len(list):
                if list[j] > list[j+1]:
                    k = lista[j+1]
                    list[j+1] = list[j]
                    list[j] = k
        self.s.setLista(list)
    def found(self, numprod):
        list= self.s.list()
        i = 0
        while i < len(list) and numprod != list[i].getnumprod():
            i += 1
            if i < len(list):
                return True
            else: 
                return False
    def pos(self, numprod):
        list = self.s.list()
        i = 0
        while i < len(list) and numprod != list[i].getnumprod():
            i += 1
        return i
    def changeHmuch(self, numprod, hmuch2):
        if self.found(numprod) :
            i = self.pos(numprod)
            list = self.s.list()
            list[i].sethmuch(hmuch2)
            return True
        else:
            return False
    def addProd(self, producto):
        self.s.enqueue(producto)
        self.notmess()
    def masmarca(self, aa):
        productos = []
        if self.s.isEmpty():
            list = self.s.list()
            for i in len(list):
                if list[i].numR > aa:
                    productos.append(list[i])
        return produtos