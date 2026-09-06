from Estruturas.Nodo import Nodo

class LSE:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.total = 0

    def esta_vazia(self):
        return self.inicio is None

    def inserir_inicio(self, valor):
        novo_nodo = Nodo(valor)

        if self.esta_vazia():
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            novo_nodo.proximo = self.inicio
            self.inicio = novo_nodo