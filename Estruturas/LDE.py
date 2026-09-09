from Nodo import Nodo


class LDE:

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

    def remover(self, codigo):
        atual = self.inicio

        while atual is not None:
            if atual.dado.get_identificador_unico() == codigo:
                if atual == self.inicio:
                    return self.remover_inicio()
                elif atual == self.fim:
                    return self.remover_fim()
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                    atual.anterior = None
                    atual.proximo = None
                    self.total -= 1
                    return atual.dado

            atual = atual.proximo

        return None

    def imprimir_lista(self):
        atual = self.inicio

        while atual is not None:
            print(atual)
            atual = atual.proximo

    def imprimir_reverso(self):
        atual = self.fim

        while atual is not None:
            print(atual)
            atual = atual.anterior

    def listar(self):
        valores = []
        atual = self.inicio

        while atual is not None:
            valores.append(atual.dado)
            atual = atual.proximo

        return valores

    def listar_inverso(self):
        valores = []
        atual = self.fim

        while atual is not None:
            valores.append(atual.dado)
            atual = atual.anterior

            return valores

    def imprimir_horizontal(self):
        atual = self.inicio
        elementos = []

        while atual is not None:
            elementos.append(f"[{atual}]")
            atual = atual.proximo

        print(" <-> ".join(elementos))

    def tamanho(self):
        return self.total

    def __len__(self):
        return self.total