class Fila:
    def __init__(self):
        self.elementos = []

    def enfileirar(self,valor):
        """Adiciona um elemento ao final da fila."""
        self.elementos.append(valor)

    def desenfileirar(self):
            """Remove e retorna o primeiro elemento da fila."""
            if self.esta_vazia():
                 return "Fila Vazia."

            return self.elementos.pop(0)

    def primeiro(self):
         """Mostra quem é o próximo da fila sem remover."""
         if self.esta_vazia():
              return "Fila vazia."

         return self.elementos[0]

    def esta_vazia(self):
         return not self.elementos

    def tamanho(self):
             return len(self.elementos)

    def limpar(self):
             """Esvazia toda a fila"""
             self.elementos.clear()

    def __str__(self):
          if self.esta_vazia():
                return "Fila: []"

          return "Fila: " + "-> ".join(map(str, self.elementos))