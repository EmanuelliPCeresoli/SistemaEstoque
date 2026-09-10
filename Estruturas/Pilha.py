class Pilha:

    def __init__(self):
        self.elementos = []

    def push(self, valor):
        """Empilha um novo elemento no topo."""
        self.elementos.append(valor)

    def pop(self):
        """Remove e retorna o elemento no topo."""
        if self.esta_vazia():
            raise IndexError("A pilha está vazia")

        topo = self.elementos.pop()
        return topo

    def peek(self):
        """Retorna ao topo sem remover."""
        if self.esta_vazia():
            raise IndexError("A Pilha está vazia.")

        return self.elementos[-1]

    def esta_vazia(self):
        return not self.elementos

    def limpar(self):
        """Remove todos os elementos da Pilha."""
        self.elementos.clear()

    def tamanho(self):
        return len(self.elementos)

    def __len__(self):
        return self.tamanho()

    def __str__(self):
        if self.esta_vazia():
            return "Pilha: []"

        return "Topo -> " + " | ".join(map(str, reversed(self.elementos)))