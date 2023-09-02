import random
class No(object):

    def __init__(self, valor, nivel):
        self.valor = valor

        self.forward = [None]*(nivel+1)

class SkipList(object):
    def __init__(self, nivelMaximo, P):
        self.NivelMaximo =  nivelMaximo
        self.P = P
        self.header = self.criaNo(self.NivelMaximo, -1)
        self.nivel = 0
    def criaNo(self, nivel, valor):
        n = No(valor, nivel)
        return n
    def nivelAleatorio(self):
        nivel = 0
        while random.random() < self.P and nivel<self.NivelMaximo:
            nivel += 1
        return nivel
    def insere(self, valor):
        update = [None]*(self.NivelMaximo + 1)
        atual = self.header

        for i in range(self.nivel, -1, -1):
            while atual.forward[i] and atual.forward[i].valor < valor:
                atual = atual.forward[i]
            update[i] = atual
        
        atual = atual.forward[0]

        if atual == None or atual.valor != valor:
            nivelaleatorio = self.nivelAleatorio()

            if nivelaleatorio > self.nivel:
                for i in range(self.nivel+1, nivelaleatorio+1):
                    update[i] = self.header
                self.nivel = nivelaleatorio
            n = self.criaNo(nivelaleatorio, valor)

            for i in range(nivelaleatorio+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n   

            print("INSERIDO COM SUCESSO VALOR {}".format(valor))

    def printaLista(self):
        print("SKIPLIST:")
        head = self.header
        for nivel in range(self.nivel+1):
            print("Level {}: ".format(nivel), end=" ")
            no = head.forward[nivel]
            while(no != None):
                print(no.valor, end=" ")
                no = no.forward[nivel]
            print("")
    
    def delete(self, valor):
        update = [None]*(self.NivelMaximo + 1)
        atual = self.header

        for i in range(self.nivel, -1, -1):
            while atual.forward[i] and atual.forward[i].valor < valor:
                atual = atual.forward[i]
            update[i] = atual
    
        atual = atual.forward[0]

        if atual and atual.valor == valor:
            for i in range(self.nivel+1):
                if update[i].forward[i] != atual:
                    break;

                update[i].forward[i] = atual.forward[i]
            
            while self.nivel > 0 and self.header.forward[self.nivel] == 0:
                self.nivel -= self.nivel
            print("CHAVE DELETADA COM SUCESSO : {}".format(valor))

    def busca(self, valor):
        atual = self.header
        for i in range(self.nivel, -1, -1):
            while atual.forward[i] and atual.forward[i].valor < valor:
                atual = atual.forward[i]
    
        atual = atual.forward[0]

        if atual and atual.valor == valor:
            print("CHAVE ENCONTRADA: {}".format(valor))


Lista = SkipList(3, 0.5)
Lista.insere(98)
Lista.insere(6)
Lista.insere(7)
Lista.insere(21)
Lista.insere(19)
Lista.insere(35)
Lista.insere(75)
Lista.insere(91)
Lista.insere(77)
Lista.insere(64)
Lista.printaLista()

Lista.busca(21)

Lista.delete(21)
Lista.printaLista()

