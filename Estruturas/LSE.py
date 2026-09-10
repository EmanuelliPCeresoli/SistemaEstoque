from Nodo import Nodo

class LSE:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.total = 0

    def esta_vazia(self):
        return self.inicio is None

    def buscar(self, codigo):
        atual = self.inicio

        while atual is not None:
            if atual.dado.get_identificador_unico() == codigo:
                return atual.dado
            atual = atual.proximo

        return None

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
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

        self.total +=1

    def remover(self, codigo):
        if self.esta_vazia():
            return None

        if self.inicio.dado.get_identificador_unico() == codigo:
            return self.remover_inicio()

        anterior = self.inicio
        atual = self.inicio.proximo

        while atual is not None:
            if atual.dado.get_identificador_unico() == codigo:
                anterior.proximo = atual.proximo

                if atual == self.fim:
                    self.fim = anterior

                atual.proximo = None
                self.total -=1
                return atual.dado

            anterior = atual
            atual = atual.proximo

        return None

    def remover_inicio(self):
        if self.esta_vazia():
            return "A lista está vazia"

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        removido.proximo = None
        self.total -=1
        return removido

    def remover_fim(self):
        if self.esta_vazia():
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

    def listar(self):
        valores = []
        atual = self.inicio

        while atual is not None:
            valores.append(atual.dado)
            atual = atual.proximo

        return valores

    def imprimir_horizontal(self):
        atual = self.inicio
        elementos = []

        while atual is not None:
            elementos.append(f"[{atual}]")
            atual = atual.proximo

        print(" -> ".join(elementos))

    def tamanho(self):
        return self.total

    def __len__(self):
        return self.total