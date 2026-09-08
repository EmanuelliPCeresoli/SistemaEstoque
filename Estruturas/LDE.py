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

        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

            self.total += 1

    def remover_inicio(self):
        if self.esta_vazia():
            return "A lista está vazia."

        removido = self.inicio

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            removido.proximo = None

        self.total -= 1
        return removido

    def remover_fim(self):
        if self.esta_vazia():
            return "A lista está vazia."

        removido = self.fim

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            removido.anterior = None

        self.total -= 1
        return removido

    def imprimir_lista(self):
        atual = self.inicio