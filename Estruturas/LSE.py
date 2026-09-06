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

        self.total += 1

    def inserir_fim(self, valor):
        novo_nodo = Nodo(valor)

        if self.esta_vazia():
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            novo_nodo.proximo = self.inicio
            self.inicio = novo_nodo

        self.total +=1

    def remover_inicio(self):
        if self.esta_vazia(self):
            return "A lista esta vazia."

        removido = self.inicio

        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
            self.total -= 1
            return removido

        anterior = self.inicio

        while anterior.proximo != self.fim:
            anterior = anterior.proximo

        anterior.proximo = None
        self.fim = anterior
        self.total -= 1

        return removido

    def imprimir_lista(self):
        atual = self.inicio

        while atual is not None:
            print(atual)
            atual = atual.proximo

    def imprimir_horizontal(self):
        atual = self.inicio
        elementos = []

        while atual is not  None:
            elementos.append(f"[{atual}]")
            atual = atual.proximo

            print(" -> ".join(elementos))

    def tamanhi(self):
        return self.total