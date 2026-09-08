class Pilha:

    def __init__(self):
        self.elementos = []

    def push(self, valor):
        """Empilha um novo elemento no topo."""
        self.elementos.append(valor)