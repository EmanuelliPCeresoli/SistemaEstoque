class Venda:
    def __init__(self, codigo, codigo_cliente, itens, valor_total= None):
        self.codigo = int(codigo)
        self.codigo_cliente = int(codigo_cliente)
        self.itens = itens

        if self.codigo <= 0:
            raise ValueError("O código da venda deve ser maior que zero.")

        if self.codigo_cliente <= 0:
            raise ValueError("O código do cliente deve ser maior que zero.")

        if len(self.itens) == 0:
            raise ValueError("É necessário ter pelo menos um produto na venda.")

        if valor_total is None:
            self.valor_total = self.calcular_total()
        else:
            self.valor_total = float(valor_total)

    def calcular_total(self):
        total = 0

        for item in self.itens:
            total += item["quantidade"] * item["preco_unitario"]

        return total

    def itens_para_texto(self):
        partes = []

        for item in self.itens:
            partes.append( 
                f"{item['codigo_produto']}:{item['quantidade']}:{item['preco_unitario']}"
                )

        return "|".join(partes)

    def to_csv_row(self):
        return [self.codigo, self.codigo_cliente, self.itens_para_texto(), self.valor_total]

    def __str__(self):
        return (f"Venda {self.codigo} | Cliente {self.codigo_cliente} | Total: R$ {self.valor_total: .2f} ")

    def itens_de_texto(texto):
        itens = []

        if texto.strip() == "":
            return itens

        partes = texto.split("|")

        for parte in partes:
            dados = parte.split(":")

            codigo_produto = int(dados[0])
            quantidade = int(dados[1])
            preco_unitario = float(dados[2])

            itens.append(
                {
                "codigo_produto": codigo_produto, 
                          "quantidade": quantidade, 
                          "preco_unitario": preco_unitario
                          }
                          )

        return itens

    def venda_from_csv_row(row):
        itens = Venda.itens_de_texto(row["itens"])
        return Venda( 
            row["codigo"],
            row["codigo_cliente"],
            itens,
            row["valor_total"]
            )