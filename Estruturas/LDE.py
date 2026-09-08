from Estruturas.Nodo import Nodo

class LDE:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.total = 0

    def esta_vazia(self):
        return self.inicio is None

    def inserir_inicio(self, valor):
        novo = Nodo(valor)

        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

        self.total += 1

    def inserir_fim(self, valor):
        novo = Nodo(valor)