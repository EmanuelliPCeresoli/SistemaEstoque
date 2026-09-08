class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = int(codigo)
        self.nome = nome.strip()
        self.preco = float(preco)
        self.quantidade = int(quantidade)

        if self.codigo <= 0:
            raise ValueError("O ID do produto deve ser maior que zero.")

        if self.nome == "":
            raise ValueError("O nome do produto não pode ficar vazio.")

        if self.preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")

        if self.quantidade < 0:
            raise ValueError("A quantidade em estoque não pode ser negativa.")

    def get_identificador_unico(self):
        return self.codigo

    def atualizar_estoque(self, nova_quantidade):
        nova_quantidade = int(nova_quantidade)

        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        self.quantidade = nova_quantidade

    def to_csv_row(self):
        return [self.codigo, self.nome, self.preco, self.quantidade]

    def __str__(self):
        return(f"Produto {self.codigo} - {self.nome} | " f"R$ {self.preco: .2f} | " f"Estoque: {self.quantidade}" )

    def produto_from_csv_row(row):
        return Produto(row["codigo"], row["nome"], row["preco"], row["quantidade"])

