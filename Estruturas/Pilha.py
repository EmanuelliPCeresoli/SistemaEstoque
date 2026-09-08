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